TRAIN_SET=train_trans.txt
TEST_SET=test_trans.txt
TRAIN_SMALL_SET=train_small_trans.txt
TRAIN_VALID_SET=train_valid_trans.txt
TRAIN_TRAIN_CV_SET=train_train_cv_
TRAIN_VALID_CV_SET=train_valid_cv_

# C = 1 / 2 lambda
LAMBDA=(0.0001 0.01 1 100 10000)
_LAMBDA=(5000 50 0.5 0.005 0.00005)

OUT=problem

printf 'Cleaning data, model and predict result ... '
sh clean.sh
printf 'Done\n'

printf 'Transforming data by the third-order polynomial transformation ... '
python3 transform_data.py
printf 'Done\n'

problem12=true
problem13=true
problem14=true
problem15=true
problem16=true

# Force to run the problem 14
if "$problem15"
then
problem14=true
fi

# the name of model will be the same for each run, so we have to rename the file if you want to save the w
if "$problem12"
then
  echo '=================================================='
  echo 'Running the problem 12'
  echo '=================================================='
  
  best_idx=0
  best_num=0
  
  for i in {0..4}
    do
      printf 'Lambda: ' 
      printf ${LAMBDA[$i]}
      printf '\t'
      ./train -s 0 -c ${_LAMBDA[$i]} -q $TEST_SET 
      acc=`./predict -b -q $TEST_SET $TEST_SET.model ${OUT}_12_${i}.result`
      echo $acc

      acc=($acc)
      acc_num=${acc[3]}
      acc_num=${acc_num%/*}
      acc_num=${acc_num:1}
      
      if [ "$acc_num" -ge "$best_num" ]
      then
        best_idx=$i
        best_num=$acc_num
      fi

  done # for i in {0..4}

  echo 'Best lambda is ' ${LAMBDA[$best_idx]}

fi # if [ $problem12 ]


if "$problem13"
then
  echo '=================================================='
  echo 'Running the problem 13'
  echo '=================================================='
  
  best_idx=0
  best_num=0
  
  for i in {0..4}
    do
      printf 'Lambda: ' 
      printf ${LAMBDA[$i]}
      printf '\t'
      ./train -s 0 -c ${_LAMBDA[$i]} -q $TRAIN_SET
      acc=`./predict -b -q $TRAIN_SET $TRAIN_SET.model ${OUT}_13_${i}.result`
      echo $acc
      
      acc=($acc)
      acc_num=${acc[3]}
      acc_num=${acc_num%/*}
      acc_num=${acc_num:1}
      
      if [ "$acc_num" -ge "$best_num" ]
      then
        best_idx=$i
        best_num=$acc_num
      fi

  done # for i in {0..4}

  echo 'Best lambda is ' ${LAMBDA[$best_idx]}

fi # if [ $problem13 ]


if "$problem14"
then
  echo '=================================================='
  echo 'Running the problem 14'
  echo '=================================================='
  
  best_idx=0
  best_num=0
  
  for i in {0..4}
    do
      printf 'Lambda: ' 
      printf ${LAMBDA[$i]}
      printf '\t'
      ./train -s 0 -c ${_LAMBDA[$i]} -q $TRAIN_SMALL_SET
      acc=`./predict -b -q $TRAIN_VALID_SET $TRAIN_SMALL_SET.model ${OUT}_14_${i}.result`
      echo $acc

      mv $TRAIN_SMALL_SET.model ${TRAIN_SMALL_SET}_${i}.model
      
      acc=($acc)
      acc_num=${acc[3]}
      acc_num=${acc_num%/*}
      acc_num=${acc_num:1}
      
      if [ "$acc_num" -ge "$best_num" ]
      then
        best_idx=$i
        best_num=$acc_num
      fi
  
  done # for i in {0..4}
  
  echo 'Best lambda is ' ${LAMBDA[$best_idx]}

  ./predict -b -q $TEST_SET ${TRAIN_SMALL_SET}_${best_idx}.model ${OUT}_14_all.result

fi # if [ $problem14 ]


if "$problem15"
then
  echo '=================================================='
  echo 'Running the problem 15'
  echo '=================================================='
  printf 'Lambda: ' 
  printf ${LAMBDA[$best_idx]}
  printf '\t'
  ./train -s 0 -c ${_LAMBDA[${best_idx}]} -q $TRAIN_SET
  acc=`./predict -b -q $TEST_SET $TRAIN_SET.model ${OUT}_15.result`
  echo $acc

fi # if [ $problem15 ]


if "$problem16"
then
  echo '=================================================='
  echo 'Running the problem 16'
  echo '=================================================='
  best_idx=0
  best_num=0
  
  for i in {0..4}
    do
      printf 'Lambda: ' 
      printf ${LAMBDA[$i]}
      printf '\n'
      acc_num=0
      for j in {0..4}
        do
          ./train -s 0 -c ${_LAMBDA[$i]} -q ${TRAIN_TRAIN_CV_SET}${j}.txt
          acc_temp=`./predict -b -q ${TRAIN_VALID_CV_SET}${j}.txt ${TRAIN_TRAIN_CV_SET}${j}.txt.model ${OUT}_16_${i}_${j}.result`
          echo $acc_temp

          acc_temp=($acc_temp)
          acc_temp_num=${acc_temp[3]}
          acc_temp_num=${acc_temp_num%/*}
          acc_temp_num=${acc_temp_num:1}

          acc_num=`expr $acc_num + $acc_temp_num`
      done
      
      if [ "$acc_num" -ge "$best_num" ]
      then
        best_idx=$i
        best_num=$acc_num
      fi
  
  done # for i in {0..4}
  
  echo 'Best lambda is ' ${LAMBDA[$best_idx]}
  echo 'Accurate number is ' $best_num

fi # if [ $problem16 ]
