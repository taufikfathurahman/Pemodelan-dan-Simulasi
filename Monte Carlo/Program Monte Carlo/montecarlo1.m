function montecarlo1(handles, function_fx, batas_atas, batas_bawah, N, K)

fx = function_fx;
interval_integral = [];
hasil_mean = [];

for i = 1000:1000:N
    hasil_fx = [];
    rand_num = batas_bawah + (batas_atas - batas_bawah).*rand(i,1);
    for j = 1:i
        x = num2str(rand_num(j));
        x = ['(' x ')'];
        new_fx = strrep(function_fx, '(x)', x);
        hasil_fx =[hasil_fx eval(new_fx)];
    end
    hasil_avg = (1/i)*sum(hasil_fx);
    varian = (1/(i-1))*sum(hasil_fx)-hasil_avg;

    nilai_integral1 = (hasil_avg+K*varian)*(batas_atas-batas_bawah);
    nilai_integral2 = (hasil_avg-K*varian)*(batas_atas-batas_bawah);
    
    p = ['(' num2str(nilai_integral2) ' <=> '];
    q = [num2str(nilai_integral1) '), '];
    
    interval_integral = [interval_integral [p q]];
    
    mean_integral = (nilai_integral1 + nilai_integral2)/2;
    hasil_mean = [hasil_mean mean_integral];
end

fx = strcat('@(x) ', fx);        
hasil_eksak = integral(eval(fx), batas_bawah, batas_atas);

set(handles.output_eksak, 'String', num2str(hasil_eksak));
set(handles.output_mc, 'String', num2str(interval_integral));

axes(handles.axes1);        
plot((1000:1000:N), repmat(hasil_eksak, size(1000:1000:N)));
hold on;
scatter((1000:1000:N), hasil_mean);
xlabel('N Values'); 
ylabel('Integration Result');
hold off;
legend('Eksak', 'Monte carlo 1');

end