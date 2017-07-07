# ==============================================================================

"""
"""
# Disable linter warnings to maintain consistency with tutorial.
# pylint: disable=invalid-name
# pylint: disable=g-bad-import-order

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import os

import tensorflow as tf
tf.__version__

tf.app.flags.DEFINE_integer('training_iteration', 1000,
                            'Number of training iterations')
tf.app.flags.DEFINE_integer('model_version', 1, 'Version number of the model')
tf.app.flags.DEFINE_string('data_dir', '/tmp/data', 'Data directory')
tf.app.flags.DEFINE_string('log_dir', 'models/log', 'Log directory')
FLAGS = tf.app.flags.FLAGS


if __name__ == '__main__':
    tf.app.run()
