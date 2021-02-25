# Datasets for benchmark

## 介绍

>  该数据库用于支持热布局温度场预测任务，数据地址：/192.168.2.1/mnt/share1/layout_data/v1.0/data/
>
>  samples中提供数据库的样例

## 数据库结构

> 数据库提供三种不同边界：小孔散热、单边散热和四周全散热

- `data`中存放不同边界数据库
  - `one_point`小孔散热边界
    - `train`存放训练数据
      - `train`训练样本存放文件夹
      - `train_val.txt`用于网络训练的数据list
    - `test`存放测试数据
      - `test`测试样本存放文件夹
      - `test_*.txt`用于测试的数据list，其中`test_0.txt`、`test_1.txt`、`test_2.txt`、`test_3.txt`、`test_4.txt`、`test_5.txt`、`test_6.txt`分别存放了不同方式采样得到的测试样本
  - `rm_wall`单边散热边界
    - `train`
      - `train`
      - `train_val.txt`
    - `test`
      - `test`
      - `test_*.txt`
  - `all_walls`四周全散热边界
    - `train`
      - `train`
      - `train_val.txt`
    - `test`
      - `test`
      - `test_*.txt`

## 组件介绍

> 布局区域是`0.1m*0.1m`方形区域，共有12个大小功率不同组件

* 组件大小、功率

  | 组件 | 长(m) | 宽(m) | 功率($W/m^2$) |
  | :--: | :---: | :---: | :-----------: |
  |  1   | 0.016 | 0.012 |     4000      |
  |  2   | 0.012 | 0.006 |     16000     |
  |  3   | 0.018 | 0.009 |     6000      |
  |  4   | 0.018 | 0.012 |     8000      |
  |  5   | 0.018 | 0.018 |     10000     |
  |  6   | 0.012 | 0.012 |     14000     |
  |  7   | 0.018 | 0.006 |     16000     |
  |  8   | 0.009 | 0.009 |     20000     |
  |  9   | 0.006 | 0.024 |     8000      |
  |  10  | 0.006 | 0.012 |     16000     |
  |  11  | 0.012 | 0.024 |     10000     |
  |  12  | 0.024 | 0.024 |     20000     |

* 组件布局示例

  | ![1](https://i.loli.net/2021/01/12/XBGU8TiWYFZ5kft.png) | ![2](https://i.loli.net/2021/01/12/72KgnHw9kNMp3bA.png) |
  | :-----------------------------------------------------: | :-----------------------------------------------------: |
  |                        Example 1                        |                        Example 2                        |

  

## 数据库详情

* train包含2000组sequence采样方式生成的训练样本 ，示例如下

  | ![Example_layout_1](https://i.loli.net/2021/01/12/TOJ3sDFzbLk8KXC.jpg) | ![Example_heat_onepoint](https://i.loli.net/2021/01/12/fkSIhy7xn8pMa6q.jpg) | ![Example_heat_leftwall](https://i.loli.net/2021/01/12/wmKXpV6Waio5jRN.jpg) | ![Example_heat_allwalls](https://i.loli.net/2021/01/12/kjcU6HKaQnY3qF4.jpg) |
  | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
  |                        heat layout                           |                          one point                           |                           rm_wall                            |                          all_walls                           |

  

* test包含不同方式获得的测试样本40000组 

  * `test_0.txt`通过sequence采样方式生成的10000组测试样本 ，示例如下
  
    | ![Seq_Example_layout_1](https://gitee.com/ChenXianqi/picbed/raw/master/img/Seq_Example_layout_1.jpg) | ![Seq_Example_layout_2](https://gitee.com/ChenXianqi/picbed/raw/master/img/Seq_Example_layout_2.jpg) | ![Seq_Example_layout_3](https://gitee.com/ChenXianqi/picbed/raw/master/img/Seq_Example_layout_3.jpg) |
    | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
    |                          Example 1                           |                          Example 2                           |                          Example 3                           |
  
    
  
  * `test_1.txt`通过gibbs方式采样生成的10000组测试样本 ，示例如下
  
    | ![Gib_Example_layout_1](https://gitee.com/ChenXianqi/picbed/raw/master/img/Gib_Example_layout_1.jpg) | ![Gib_Example_layout_2](https://gitee.com/ChenXianqi/picbed/raw/master/img/Gib_Example_layout_2.jpg) | ![Gib_Example_layout_3](https://gitee.com/ChenXianqi/picbed/raw/master/img/Gib_Example_layout_3.jpg) |
    | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
    |                          Example 1                           |                          Example 2                           |                          Example 3                           |
  
    
  
  * `test_2.txt`功率相同或相近组件相邻构成的特殊组件布局样本，共有4类情况，每类情况1000组测试样本 ，示例如下
  
    | ![image-20210111171838305](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111171838305.png) | ![image-20210111171953807](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111171953807.png) | ![image-20210111172012636](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172012636.png) | ![image-20210111172030261](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172030261.png) |
    | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
    | ![image-20210111171926941](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111171926941.png) | ![image-20210111172002098](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172002098.png) | ![image-20210111172021046](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172021046.png) | ![image-20210111172040989](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172040989.png) |
    |                         8和12号组件                          |                        2和7和10号组件                        |                         5和11号组件                          |                          4和9号组件                          |
  
  
  
  * `test_3.txt`组件布局密集在上半部，1/5区域，2/5区域，3/5区域，4/5区域，或下半部的测试样本，各1000组 ，示例如下
  
    | ![image-20210111172439250](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172439250.png) | ![image-20210111172443301](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172443301.png) | ![image-20210111172447170](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172447170.png) | ![image-20210111172450326](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172450326.png) | ![image-20210111172454168](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172454168.png) | ![image-20210111172458093](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172458093.png) |
    | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
    |                            上半部                            |                           1/5区域                            |                           2/5区域                            |                           3/5区域                            |                           4/5区域                            |                            下半部                            |
  
  * `test_4.txt`组件布局密集在左半部，1/5区域，2/5区域，3/5区域，4/5区域，或右半部的测试样本，各1000组 ，示例如下
  
    | ![image-20210111172237190](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172237190.png) | ![image-20210111172256130](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172256130.png) | ![image-20210111172259807](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172259807.png) | ![image-20210111172303662](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172303662.png) | ![image-20210111172307118](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172307118.png) | ![image-20210111172311214](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172311214.png) |
    | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
    |                            左半部                            |                           1/5区域                            |                           2/5区域                            |                           3/5区域                            |                           4/5区域                            |                            右半部                            |
  
  * `test_5.txt`组件布局在内部较小方形区域测试样本，共考虑100x100​区域，120x120区域，​140x140区域3种情况，各1000组测试样本 ，示例如下
  
    | ![image-20210111172627957](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172627957.png) | ![image-20210111172731192](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172731192.png) | ![image-20210111172741897](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172741897.png) |
    | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
    | ![image-20210111172644322](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172644322.png) | ![image-20210111172737654](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172737654.png) | ![image-20210111172745392](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172745392.png) |
    |                        100x100                        |                        120x120                        |                        140x140                        |
  
    
  
  * `test_6.txt`最大功率布局在角落中的特殊样本，共1000组测试样本，示例如下
  
    | ![image-20210111172945696](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111172945696.png) | ![image-20210111173016784](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111173016784.png) | ![image-20210111173020434](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111173020434.png) | ![image-20210111173026738](https://gitee.com/ChenXianqi/picbed/raw/master/img/image-20210111173026738.png) |
    | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
    |                            右下角                            |                            左上角                            |                            左下角                            |                            左下角                            |
  
    

## 其他