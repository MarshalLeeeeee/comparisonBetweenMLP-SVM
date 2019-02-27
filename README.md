<h1>comparisonBetweenMLP-SVM</h1>
<p>To compare the performance between MLP and SVM structure, I determine 3 aspects to be examed, the classified number, the sample number and the feature dimensions. I normalized and shuffled each data set and segmentd them into train-set and test-set with proportion 9 to 1.</p>

<h3> Requirements </h3>
<ul type = 'disc'>
  <li>sklearn</li>
</ul>

<h3> Datasets </h3>
<p> You can get them from <a href="https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/"> here</a>.</p>
<table frame="vsides">
  <tr>
  	<th>Dataset</th>
    <th>Class Number</th>
    <th>Sample Number</th>
    <th>Feature Number</th>
  </tr>
  <tr>
    <td>liver-disorder</td>
    <td>2</td>
    <td>345</td>
    <td>5</td>
  </tr>
  <tr>
    <td>leukemia</td>
    <td>2</td>
    <td>72</td>
    <td>7129</td>
  </tr>
  <tr>
    <td>cod-ma</td>
    <td>2</td>
    <td>59535</td>
    <td>8</td>
  </tr>
  <tr>
    <td>vowel</td>
    <td>11</td>
    <td>690</td>
    <td>10</td>
  </tr>
  <tr>
    <td>SVHN</td>
    <td>10</td>
    <td>26832</td>
    <td>3072</td>
  </tr>
  <tr>
    <td>dna</td>
    <td>3</td>
    <td>5186</td>
    <td>180</td>
  </tr>
  <tr>
    <td>shuttle</td>
    <td>7</td>
    <td>58000</td>
    <td>9</td>
  </tr>
  <tr>
    <td>rcv1.multiclass</td>
    <td>53</td>
    <td>534135</td>
    <td>47236</td>
  </tr>
</table>

<h3> Details </h3>
<p> I conducted the experiment by the aid of sklearn library. sklearn.svm.SVC() is used to make the svm model and sklearn.neural_network.MLPClassifier() is used to make the multi-layer perception neural network (actually it precisely is a network with one input layer, one hidden layer and one output layey).</p>
<p> I changed the argument:kernel as the alternative kernel function in SVC() from ['linear', 'poly', 'rbf', 'sigmoid'] and I changed the argument:activation as the alternative active function in MLPClassifier() from ['identity', 'logistic', 'tanh', 'relu']. </p>

<h3> Results </h3>
<p> Results are shown in <a href="https://github.com/MarshalLeeeeee/comparisonBetweenMLP-SVM/tree/master/demo"> demo </a>.</p>

<h3> Conclusion </h3>
<p> For svm model, kernel function as linear and rbf works better that the other 2 kernels in whatever dataset, especially better than the poly kernel since we have to carefully decide the polynomial degree as well as the regulation coefficient. For dataset with larger sample number and small feature dimensions, svm can work well. So does for dataset with unsufficient sample number and considerable feature dimensions. But for dataset with both unsufficient sample number and feature dimensions, svm does not perform good enough. </p>

<p> For mlp model, activation function as relu almost works the better for all the dataset. It is most obvious for the scenario that both sample number and feature dimension are small (dataset liver-disorders and vowel) where relu works better than the other activation functions. It is not clear, however, for me to explain the reason why. But via many neural networks which use relu as activation function, the superiority of relu in many cases can be proved. Still, when it comes to the dataset, mlp works better on the dataset with more samples with low feature dimension (like cod-ma and shuttle). Meanwhile, given the dataset that has large feature dimension and scant sample number, mlp works unstablely. By varing the number of hidden units, the result may be totally diffenrent and unpredictable, thus mlp is not good to fit such dataset.</p>

<p> Compared the two models, both perform in binary classification preoblem as well as multiclass ones. SVM may work better than mlp in dataset with unsufficient sample number and considerable feature dimensions but worsely in dataset with quantitive sample number and scant feature dimensions. One explaination I might give is that svm is prone to find the difference between different labels while neural network tends to find a gerenal rule to classify the data into corresponding labels. Therefore for dataset with unsufficient sample number and considerable feature dimensions, it is easier to figure out the margin but harder to conclude the general principle by 'learning'. In contrast, dataset with considerable samples may be representative enough to summarize the general model, nevertheless to find the margin to more difficult because we have to balance the acuuracy, regularization and the penalty terms. </p>

<p> The experiment is not perfect and something can be improved. For instance, the predict accuracy may be improved by varying the parameters. Therefore the result can have some bias. Still, due to the restriction of the hardware, some more representative dataset is unable to be tried because of MemoryError or the fit time is too long to make me know whether the program is executed or not. </p>

<h3> Extra trial on deep learning datasets </h3>
<p> I used cifar-10 as the dataset in this section. With the traditional SVC() function, the dataset is too large to be fed to the model. sklearn.svm.SVC() does not support the batch learning so I use sklearn.linear_model.SGDClassifier() as the alternative because it supports the batch learning. With the parameter:loss set as defaultas 'hinge', the model give a linear SVM. By varing some alternative parameters, the best accuracy I get is 0.3098. </p>>

<p> Compares to the current benchmark on cifar-10, varying from 75.86% to 96.53%, the accuracy in linear SVM is poor enough. Since the input of the svm is the vector, with the loss of the structure information of the picture, the output is apparently low. With the deep CNN, the current state-out-art technique can extract the feature of the picture better, and by deconvolution we can find CNN get some significant picture fraction or concept from the original input image through learning. In summary, the svm is not proper for image processing. </p>