income = 2500;

rent = 1200;
utils = 300; % water, electricity, internet, etc.
car = 250;
food = 300;
phone = 50;
retirement = .1 * income;

outflow = rent + utils + car + food + phone + retirement;

nonessentials = income - outflow;

perday = nonessentials / 30;

disp([ 'I can spend ' num2str(perday) ' extra each day.'])

perweek = nonessentials / (30/7);
inThirds = perweek / 3;
disp([' I can spend ' num2str(inThirds*2) ' during the weekend, and ' ...
    num2str(inThirds/5) ' each week day.'])