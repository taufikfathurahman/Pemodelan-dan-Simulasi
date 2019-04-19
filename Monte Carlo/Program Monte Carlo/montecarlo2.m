function montecarlo2(handles, function_fx, batas_atas, batas_bawah, f_min, f_max, N)

fx = function_fx;
hasil_integral = [];

for i = 1000:1000:N
    Q = 0;
    for j = 1:i
        Xi = batas_bawah + (batas_atas - batas_bawah).*rand();
        Yi = f_min + (f_max - f_min).*rand();

        x = ['(' num2str(Xi) ')'];
        new_fx = strrep(function_fx, '(x)', x);
        hasil_fx = eval(new_fx);

        if hasil_fx >= Yi
            Q = Q + 1;
        end
    end
    I = (Q/i)*(f_max-f_min)*(batas_atas-batas_bawah);
    hasil_integral = [hasil_integral I];
end
 
fx = strcat('@(x) ', fx);        
hasil_eksak = integral(eval(fx), batas_bawah, batas_atas);

set(handles.output_eksak, 'String', num2str(hasil_eksak));
set(handles.output_mc, 'String', num2str(hasil_integral));

axes(handles.axes1);        
plot((1000:1000:N), repmat(hasil_eksak, size(1000:1000:N)));
hold on;
scatter((1000:1000:N), hasil_integral);
xlabel('N Values'); 
ylabel('Integration Result');
hold off;
legend('Eksak', 'Monte carlo 2');

end