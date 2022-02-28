positiveImage = imread('CameraMan.tif');
figure
imshow(positiveImage);
negativeImage = 255 - positiveImage;
figure
imshow(negativeImage)
% element wise operation 