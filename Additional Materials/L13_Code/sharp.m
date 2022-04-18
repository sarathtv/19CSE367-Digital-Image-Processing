%a = imread('peppers.png');
a = imread('raindrop.png');
imshow(a)
title('Original Image');
b = imsharpen(a);
figure, imshow(b)
title('Sharpened Image');