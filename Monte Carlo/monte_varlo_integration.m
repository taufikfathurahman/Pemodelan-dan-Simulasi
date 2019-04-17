function varargout = monte_varlo_integration(varargin)
% MONTE_VARLO_INTEGRATION MATLAB code for monte_varlo_integration.fig
%      MONTE_VARLO_INTEGRATION, by itself, creates a new MONTE_VARLO_INTEGRATION or raises the existing
%      singleton*.
%
%      H = MONTE_VARLO_INTEGRATION returns the handle to a new MONTE_VARLO_INTEGRATION or the handle to
%      the existing singleton*.
%
%      MONTE_VARLO_INTEGRATION('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in MONTE_VARLO_INTEGRATION.M with the given input arguments.
%
%      MONTE_VARLO_INTEGRATION('Property','Value',...) creates a new MONTE_VARLO_INTEGRATION or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before monte_varlo_integration_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to monte_varlo_integration_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help monte_varlo_integration

% Last Modified by GUIDE v2.5 17-Apr-2019 19:48:12

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @monte_varlo_integration_OpeningFcn, ...
                   'gui_OutputFcn',  @monte_varlo_integration_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before monte_varlo_integration is made visible.
function monte_varlo_integration_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to monte_varlo_integration (see VARARGIN)

% Choose default command line output for monte_varlo_integration
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes monte_varlo_integration wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = monte_varlo_integration_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in hitung_button.
function hitung_button_Callback(hObject, eventdata, handles)
% hObject    handle to hitung_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
function_fx = get(handles.input_fx, 'String');
batas_atas = get(handles.batas_atas, 'String');
batas_bawah = get(handles.batas_bawah, 'String');
N = get(handles.nilai_n, 'String');
K = get(handles.nilai_k, 'String');

batas_atas = str2double(batas_atas);
batas_bawah = str2double(batas_bawah);
N = str2double(N);
K = str2double(K);

selected_method = get(get(handles.metode_integral,'SelectedObject'), 'string');
switch selected_method
    case 'Eksak'
        function_fx = strcat('@(x) ', function_fx);
        hasil = integral(eval(function_fx), batas_bawah, batas_atas);
        set(handles.output_eksak, 'String', num2str(hasil));
    case 'Monte Carlo 1'
        montecarlo1(handles, function_fx, batas_atas, batas_bawah, N);
    case 'Monte Carlo 2'
        montecarlo2(handles, function_fx, batas_atas, batas_bawah, N, K);
%     case 'Rectangular'
%         
%     case 'Trapezoidal'
end

% --- Executes on button press in one.
function one_Callback(hObject, eventdata, handles)
% hObject    handle to one (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '1');
set(handles.input_fx, 'String', str);

% --- Executes on button press in two.
function two_Callback(hObject, eventdata, handles)
% hObject    handle to two (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '2');
set(handles.input_fx, 'String', str);

% --- Executes on button press in three.
function three_Callback(hObject, eventdata, handles)
% hObject    handle to three (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '3');
set(handles.input_fx, 'String', str);

% --- Executes on button press in four.
function four_Callback(hObject, eventdata, handles)
% hObject    handle to four (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '4');
set(handles.input_fx, 'String', str);

% --- Executes on button press in five.
function five_Callback(hObject, eventdata, handles)
% hObject    handle to five (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '5');
set(handles.input_fx, 'String', str);

% --- Executes on button press in six.
function six_Callback(hObject, eventdata, handles)
% hObject    handle to six (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '6');
set(handles.input_fx, 'String', str);

% --- Executes on button press in seven.
function seven_Callback(hObject, eventdata, handles)
% hObject    handle to seven (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '7');
set(handles.input_fx, 'String', str);

% --- Executes on button press in eight.
function eight_Callback(hObject, eventdata, handles)
% hObject    handle to eight (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '8');
set(handles.input_fx, 'String', str);

% --- Executes on button press in nine.
function nine_Callback(hObject, eventdata, handles)
% hObject    handle to nine (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '9');
set(handles.input_fx, 'String', str);

% --- Executes on button press in zero.
function zero_Callback(hObject, eventdata, handles)
% hObject    handle to zero (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '0');
set(handles.input_fx, 'String', str);


% --- Executes on button press in square.
function square_Callback(hObject, eventdata, handles)
% hObject    handle to square (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, 'sqrt');
set(handles.input_fx, 'String', str);

% --- Executes on button press in exponent.
function exponent_Callback(hObject, eventdata, handles)
% hObject    handle to exponent (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, 'exp');
set(handles.input_fx, 'String', str);

% --- Executes on button press in power.
function power_Callback(hObject, eventdata, handles)
% hObject    handle to power (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '^');
set(handles.input_fx, 'String', str);

% --- Executes on button press in phi.
function phi_Callback(hObject, eventdata, handles)
% hObject    handle to phi (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, 'pi');
set(handles.input_fx, 'String', str);

% --- Executes on button press in multiplication.
function multiplication_Callback(hObject, eventdata, handles)
% hObject    handle to multiplication (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '*');
set(handles.input_fx, 'String', str);

% --- Executes on button press in division.
function division_Callback(hObject, eventdata, handles)
% hObject    handle to division (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '/');
set(handles.input_fx, 'String', str);

% --- Executes on button press in plus.
function plus_Callback(hObject, eventdata, handles)
% hObject    handle to plus (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '+');
set(handles.input_fx, 'String', str);

% --- Executes on button press in minus.
function minus_Callback(hObject, eventdata, handles)
% hObject    handle to minus (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '-');
set(handles.input_fx, 'String', str);

% --- Executes on button press in eks.
function eks_Callback(hObject, eventdata, handles)
% hObject    handle to eks (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, 'x');
set(handles.input_fx, 'String', str);


function batas_atas_Callback(hObject, eventdata, handles)
% hObject    handle to batas_atas (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of batas_atas as text
%        str2double(get(hObject,'String')) returns contents of batas_atas as a double


% --- Executes during object creation, after setting all properties.
function batas_atas_CreateFcn(hObject, eventdata, handles)
% hObject    handle to batas_atas (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function batas_bawah_Callback(hObject, eventdata, handles)
% hObject    handle to batas_bawah (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of batas_bawah as text
%        str2double(get(hObject,'String')) returns contents of batas_bawah as a double


% --- Executes during object creation, after setting all properties.
function batas_bawah_CreateFcn(hObject, eventdata, handles)
% hObject    handle to batas_bawah (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in kurung_buka.
function kurung_buka_Callback(hObject, eventdata, handles)
% hObject    handle to kurung_buka (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '(');
set(handles.input_fx, 'String', str);

% --- Executes on button press in kurung_tutup.
function kurung_tutup_Callback(hObject, eventdata, handles)
% hObject    handle to kurung_tutup (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, ')');
set(handles.input_fx, 'String', str);

% --- Executes on button press in dot.
function dot_Callback(hObject, eventdata, handles)
% hObject    handle to dot (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str = get(handles.input_fx, 'String');
str = strcat(str, '.');
set(handles.input_fx, 'String', str);



function nilai_n_Callback(hObject, eventdata, handles)
% hObject    handle to nilai_n (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of nilai_n as text
%        str2double(get(hObject,'String')) returns contents of nilai_n as a double


% --- Executes during object creation, after setting all properties.
function nilai_n_CreateFcn(hObject, eventdata, handles)
% hObject    handle to nilai_n (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function nilai_k_Callback(hObject, eventdata, handles)
% hObject    handle to nilai_k (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of nilai_k as text
%        str2double(get(hObject,'String')) returns contents of nilai_k as a double


% --- Executes during object creation, after setting all properties.
function nilai_k_CreateFcn(hObject, eventdata, handles)
% hObject    handle to nilai_k (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
