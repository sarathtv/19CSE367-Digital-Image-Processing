%clear
clear all
close all
clc
a1 = imread('spine.tif'); % Read the image
a = double(a1)/255; % Normalized Image
c = 2; % Constant
f = c*log(1 + (a)); % Log Transform
subplot(1,2,1),imshow(a1),title('Original Image');
subplot(1,2,2),imshow((f)),title('Log Transformation Image');