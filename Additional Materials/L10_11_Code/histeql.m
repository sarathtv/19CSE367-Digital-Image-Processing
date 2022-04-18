I=imread('pout.tif');
figure
subplot(1,3,1)
imshow(I)
subplot(1,3,2)
imhist(I);
counts = histcounts(I);
cdf = cumsum(counts) / sum(counts);
subplot(1,3,3)
plot(cdf);

%hist equalization and its cdf

j=histeq(I);
figure
subplot(1,3,1)
imshow(j)
subplot(1,3,2)
imhist(j,64)
counts = histcounts(j);
cdf = cumsum(counts) / sum(counts);
subplot(1,3,3)
plot(cdf);