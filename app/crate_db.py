from app import db
db.create_all()

# import tensorflow as tf
#
# hello_op = tf.constant("Hello, TensorFlow!")
# a = tf.constant(10)
# b = tf.constant(37)
# compute_op = tf.add(a,b)
#
# with tf.Session() as sess:
#     print(sess.run(hello_op))
#     print(sess.run(compute_op))

# import tensorflow as tf
# import numpy.random as random
#
# #占位符shape不设时会按传入参数自行匹配
# node1 = tf.placeholder(tf.float32)  # , shape=[4, 5])
# node2 = tf.placeholder(tf.float32)  # , shape=[4, 5])
# op = tf.multiply(node1, node2)
# session = tf.Session()
# const1 = tf.constant([1,2,3,4],shape=[2,2])
# const2 = tf.constant([1,2,3,4],shape=[2,2])
# #可以传入初始化后的常量
# print(session.run(op, {node1: session.run(const1), node2: session.run(const2)}))
# #也可以直接传入张量，其实同初始化后的常量一致
# print(session.run(op, {node1: random.rand(2, 3), node2: random.rand(2, 3)}))