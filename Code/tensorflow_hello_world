import tensorflow as tf

## Hello World
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))


## Simple addition
a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a + b))


## Query for devices
from tensorflow.python.client import device_lib

def get_available_devices():
    # See https://www.tensorflow.org/versions/r0.12/how_tos/using_gpu/index.html for documentation on devices
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos]
    
get_available_devices()
