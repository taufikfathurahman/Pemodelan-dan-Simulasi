function montecarlo1(handles, function_fx, batas_atas, batas_bawah, N, K)

hasil_integral = [];

for i = 1000:100:N
    hasil_fx = [];
    rand_num = batas_bawah + (batas_atas - batas_bawah).*rand(i,1);
    for j = 1:i
        x = num2str(rand_num(j));
        x = ['(' x];
        x = [x ')'];
        new_fx = strrep(function_fx, '(x)', x);
        hasil_fx =[hasil_fx eval(new_fx)];
    end
    hasil_avg = (1/i)*sum(hasil_fx);
    varian = (1/(i-1))*sum(hasil_fx)-hasil_avg;

    nilai_integral1 = (hasil_avg+K*varian)*(batas_atas-batas_bawah);
    nilai_integral2 = (hasil_avg-K*varian)*(batas_atas-batas_bawah);
    mean_integral = (nilai_integral1 + nilai_integral2)/2;
    hasil_integral = [hasil_integral mean_integral];
end

axes(handles.axes1);
plot((1000:100:N), hasil_integral)

end