https://github.com/openalpr/openalpr
https://github.com/openalpr/openalpr/archive/refs/tags/v2.3.0.zip
https://github.com/openalpr/openalpr/releases/download/v2.3.0/openalpr-2.3.0-win-64bit.zip

1.download openal packegs
 - src: openalpr-2.3.0.zip
 - windows Binaries: openalpr-2.3.0-win-64bit.zip

2. install openalpr python package
 cd .\openalpr-2.3.0\src\bindings\python
 python setup.py install

3. detection
 - modify 'binary_path' variable in main.py to your openALPR binary path
   for example:
   binary_path = r"c:\openALPR\openalpr_64" or
   binary_path = os.path.join(os.getcwd(), r"..\openalpr_64")

 - python main.py  car.jpg
