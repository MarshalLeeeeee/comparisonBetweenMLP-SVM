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
</table>

<h3> Conclusion </h3>