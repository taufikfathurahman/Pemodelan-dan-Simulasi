f = '3*((x).^2)';
N = 10000;

r = -5 + (5+5).*rand(N,1);

hasil = [];
k = 1.5;

for n = 1:N
    x = num2str(r(n));
    x = ['(' x];
    x = [x ')'];
    new_f = strrep(f, 'x', x);
    hasil =[hasil eval(new_f)];
end
hasil_avg = (1/N)*sum(hasil);
varian = (1/(N-1))*sum(hasil)-hasil_avg

ip = (hasil_avg+k*varian)*(5+5)
ip = (hasil_avg-k*varian)*(5+5)
