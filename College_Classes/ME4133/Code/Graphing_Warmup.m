%%%%% Donovan Gegg 
% 3/30/2022
% Code for ME 4133 Machine Design I
% Project I: Plotting Kinematic Data
% Code Purpose: Legibly Graph the provided data on 3 graphs. 

%%%%%%%%%%%%%
% Data Format
%%%%%%%%%%%%%
%%% INPUT: theta2 (rad)
    % *** Applies to ALL graphs ***
%%% OUTPUTS:
    % Graph 1: Position
        % theta3 (rad), R3 (in), R4 (in), R5 (in)
    % Graph 2: 1st Order Kinematic Coefficients 
        % h3 (none), f3 (in), f4 (in), f5 (in)
    % Graph 3: 2nd Order Kinematic Coefficients
        % h3p (none), f3p (in), f4p (in), f5p (in)
    %%% Mins, Maxes, and x intercepts are denoted by red stars

%%%%%%%
% Code
%%%%%%%

% Ensuring everything's cleared. 
close all
clc
clear

% *** Setting up all the vectors for graphing. ***

% Importing provided data as a matrix.
% Allows for easy column extraction as vectors. 
data =  readmatrix('Project I Plotting Fall 2020.xlsx');

% Input Data. Applies to ALL graphs.
theta2 = data(:,1);

% Graph 1: Position Data. 
theta3 = data(:,2);
R3 = data(:,3);
R4 = data(:,4);
R5 = data(:,5);

% Graph 2: 1st Order Kinematic Coefficients Data
h3 = data(:,6);
f3 = data(:,7);
f4 = data(:,8);
f5 = data(:,9);

% Graph 3: 2nd Order Kinematic Coefficients Data
h3p = data(:,10);
f3p = data(:,11);
f4p = data(:,12);
f5p = data(:,13);

% *** Graphing ***

% Graph 1: Position Graph. 
% Creating and naming figure 
figure('Name','Position Analysis')
grid on

% Adding dotted line for x axis for visual aid.
yline(0,'--');
hold on 

% Plot 1: theta 3
Lab_0_Plotting(theta2,theta3,true,true);
% Plot 2: R3
Lab_0_Plotting(theta2,R3,true,true);
% Plot 3: R4
Lab_0_Plotting(theta2,R4,true,true);
% Plot 4: R5
Lab_0_Plotting(theta2,R5,true,true);

% Setting x boundaries. 
xlim([0,(2*pi)]);

% Creating x ticks and labels
xticks([0,pi/4,pi/2,3*pi/4,pi,5*pi/4,3*pi/2,7*pi/4,2*pi]);
xticklabels({'0','\pi/4','\pi/2','3\pi/4','\pi','5\pi/4','3\pi/2','7\pi/4','2\pi'});

% Labeling title, x axis, & y axis.
title('Position Analysis','FontSize',20);
xlabel('\Theta2 (radians)','FontSize',18);
ylabel('Outputs','FontSize',18);

% Creating Legend
legend('','\Theta3 (radians)','','','R3 (in)','','','R4 (in)','','','R5 (in)','','');

% Ending the plots
hold off 

% Graph 2: 1st Order Kinematic Coefficients Graph.
% Creating and naming figure 
figure('Name','1st Order Kinematic Coefficients')
grid on

% Adding dotted line for x axis for visual aid.
yline(0,'--');
hold on 

% Plot 1: h3
Lab_0_Plotting(theta2,h3,true,true);
% Plot 2: f3
Lab_0_Plotting(theta2,f3,true,true);
% Plot 3: f4
Lab_0_Plotting(theta2,f4,true,true);
% Plot 4: f5
Lab_0_Plotting(theta2,f5,true,true);

% Setting x boundaries. 
xlim([0,(2*pi)]);

% Creating x ticks and labels
xticks([0,pi/4,pi/2,3*pi/4,pi,5*pi/4,3*pi/2,7*pi/4,2*pi]);
xticklabels({'0','\pi/4','\pi/2','3\pi/4','\pi','5\pi/4','3\pi/2','7\pi/4','2\pi'});

% Labeling title, x axis, & y axis.
title('1st Order Kinematic Coefficients','FontSize',20);
xlabel('\Theta2 (radians)','FontSize',18);
ylabel('Outputs','FontSize',18);

% Creating Legend
legend('','h3 (-)','','','','f3 (in)','','','','f4 (in)','','','','f5 (in)','');

% Ending the plots
hold off 

% Graph 3: 2nd Order Kinematic Coefficients Graph. 
% Creating and naming figure 
figure('Name','2nd Order Kinematic Coefficients')
grid on

% Adding dotted line for x axis for visual aid.
yline(0,'--');
hold on 

% Plot 1: h3p
Lab_0_Plotting(theta2,h3p,true,true);
% Plot 2: f3p
Lab_0_Plotting(theta2,f3p,true,true);
% Plot 3: f4p
Lab_0_Plotting(theta2,f4p,true,true);
% Plot 4: f5p
Lab_0_Plotting(theta2,f5p,true,true);

% Setting x boundaries. 
xlim([0,(2*pi)]);

% Creating x ticks and labels
xticks([0,pi/4,pi/2,3*pi/4,pi,5*pi/4,3*pi/2,7*pi/4,2*pi]);
xticklabels({'0','\pi/4','\pi/2','3\pi/4','\pi','5\pi/4','3\pi/2','7\pi/4','2\pi'});

% Labeling title, x axis, & y axis.
title('2nd Order Kinematic Coefficients','FontSize',20);
xlabel('\Theta2 (radians)','FontSize',18);
ylabel('Outputs (radians)','FontSize',18);

% Creating Legend
legend('','h3p (-)','','','','f3p (in)','','','','f4p (in)','','','','f5p (in)','');

% Ending the plots
hold off 

% *** Functions ***
% Function to Plot given inputs and outputs WITH local maxes and local mins if desired
function Lab_0_Plotting(x,y,locals,xints)
    % Plotting main graph
    plot(x,y);
    hold on
    % If local mins and maxes are desired
    if locals == true
        % Finding Local Minimums
        local_min = islocalmin(y);
        % Finding Local Maximums
        local_max = islocalmax(y);
        % Plotting Local Maxes and Mins
        plot(x(local_min),y(local_min),'r*',x(local_max),y(local_max),'r*');
        hold on
    end
    
    % If want x intercepts, call the x intercept function
    if xints == true
        Lab_0_x_int(x,y);
    end
end

% Function to find x intercepts and plot them.
function Lab_0_x_int(x,y)
    % initializing counter/indexer and current values and empty vectors
    i = 1;
    current_val = 0;
    x_zero = [];
    y_zero = [];

    % Looping thru length of input vector 
    while i <= length(y)
        % Recording previous value 
        previous_val = current_val;
        % Setting current value 
        current_val = y(i);
        % Comparing current and previous values 
        if previous_val < 0 && current_val > 0
            % Averaging the points to estimate the x value 
            est_zero = (x(i-1)+x(i))/2;
            % Concatenating vectors
            x_zero(end+1) = est_zero;
            y_zero(end+1) = 0;
        % Comparing current and previous values 
        elseif previous_val > 0 && current_val < 0
            % Averaging the points to estimate the x value 
            est_zero = (x(i-1)+x(i))/2;
            % Concatenating vectors
            x_zero(end+1) = est_zero;
            y_zero(end+1) = 0;
        end
        i = i + 1;
    end

    % Plotting the concatenated values
    plot(x_zero,y_zero,'b*');
    hold on 
end
