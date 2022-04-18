%a=imread('car_3.jpg');
a=imread('darkimage.jpg');
I=rgb2gray(a);
figure
subplot(1,2,1)
imshow(I)
subplot(1,2,2)
imhist(I)