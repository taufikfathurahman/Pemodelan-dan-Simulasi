for i = 1000:1000:10000
    hasil_fx = [];
    rand_num = batas_atas + (batas_atas - batas_bawah).*rand(i,1);
    for j = 1:i
        x = num2str(rand_num(j));
        x = ['(' x];
        x = [x ')'];
        new_fx = strrep(function_fx, 'x', x);
        hasil_fx =[hasil_fx eval(new_fx)];
    end
    hasil_avg = (1/i)*sum(hasil_fx)
    varian = (1/(i-1))*sum(hasil_fx)-hasil_avg

    ip = (hasil_avg+K*varian)*(batas_atas-batas_bawah)
    im = (hasil_avg-K*varian)*(batas_atas-batas_bawah)
end
