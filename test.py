import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print('gpu', tf.test.is_gpu_available())
a = tf.constant(2.)
b = tf.constant(3.)
print(a*b)
