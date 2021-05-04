# Classification_chemystry
基于CNN的化学物质识别



#配置Tensorflow环境

  1.在Anaconda Jupiter的Navigator中配置一个基础环境，然后下载Tensorflow包
  2.在PyCharm中Files -> Settings -> Project:XXX ->Python Interperter ,然后选中刚刚创建的Tensorflow环境作为解释器
  
  
#XX.py文件的作用讲解（按照模型的构建顺序）
  
  1.dataselect.py
      
      这个文件主要是针对图片的生成，也就是对仅存的图片进行大量的剪裁（通过旋转，平移，拉伸等操作）使得图片生成100张
      
      from keras.preprocessing.image import ImageDataGenerator 引入了一个 ImageDataGenerator 构造器，通过这个构造器进行生成图片
      
      -------
      counter = 0
      for batch in datagen.flow(x, batch_size=4 , save_to_dir='generater_pic', save_prefix=prefix, save_format='jpg'):
          counter += 1
          if counter > 100:
              break  # 否则生成器会退出循环
      -------
      通过以上这个函数将生成的图片进行保存，明显if语句限制了生成图片的张数
      
      
  2.img_to_h5.py
  
      这个文件集成了对图片的压缩和将图片保存为.h5数据集文件的功能
      
      a) 图片压缩 resize_img():
      
          TensorFlow中提供了四种缩放算法：双线性插值法（Bilinear interpolation）、最近邻居法（Nearest neighbor interpolation）、双三次插值法（Bicubic interpolation）和面积插值法（area interpolation）
          此代码中压缩图片采用的面积插值法，并且大小统一为64*64
      
      b) 图片转换 image_to_h5():
      
          此函数中，变量Y则是分类图片的标签，可自行设定（把矩阵存进h5文件时，此时标签一定要对应每一张图片（矩阵））。
          首先把图片转成RGB矩阵，即每个图片是一个64*64*3的矩阵（因为是彩色图片，所以通道是3）
      
   3.cnn.py   
      
      显然这是模型文件，同时也是训练模型函数所在地方
      
      把数据集划分为训练集和测试集，然后先坐下归一化，把标签转化为one-hot向量表示 （由load_dataset()实现）
      
      构建CNN模型，这里用了最简单的类LeNet-5，具体两层卷积层、两层池化层、一层全连接层，一层softmax输出。具体的小trick有：dropout、relu、regularize、mini-batch、adam
      
      我训练模型跑了七个小时的样子，根据电脑的性能不同，Tensorflow版本不同，会有不一样的训练效果
      
   4.load_pb_model.py
      
      这个文件则是对已经训练好的model进行测试，一定要对待测试的图片进行剪裁，大小为64*64，否则无法载入图片。
      
   
   5.其余文件
   
      功能补充，可自行添加，不是最基本的功能文件 
      
      
#注意事项

    一定不要把tensorflow版本升太高了，会导致部分函数被取消以及库之间的冲突。（不嫌麻烦想钻研版本更新的自己就去官网查取缔的函数怎么用吧）
    总之很多包的版本都不宜太高，如果有函数不存在找不到的情况，请对自己相应的库进行降级或者升级操作（File -> Settings -> Project:XXX -> Python Interpreter中修改版本）
