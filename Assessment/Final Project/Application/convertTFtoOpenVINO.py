import tensorflow as tf

model = tf.keras.models.load_model('model.h5')
tf.saved_model.save(model, 'saved_model_directory')