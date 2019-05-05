program Parse03;
{$Apptype Console}
uses
  SysUtils;
const
  TAB = ^I;
var
  Look: char;              { Lookahead Character }

{ Read new character from input stream }
procedure GetChar;
begin
  Read(Look);
end;

{ Report an error }
procedure Error(s : string);
begin
  WriteLn;
  WriteLn(^G, 'Error: ', s, '.');
  ReadLn;
  ReadLn;
end;

{ Report error and halt }
procedure Abort(s : string);
begin
  Error(s);
  Halt;
end;

{ Report what was expected }
procedure Expected(s : string);
begin
  Abort(s + ' Expected');
end;

{ Match a specific input character }
procedure Match(x : char);
begin
  if Look = x then
    GetChar
  else
    Expected('''' + x + '''');
end;

{ Recognize an alpha character }
function IsAlpha(c : char): boolean;
begin
  IsAlpha := UpCase(c) in ['A'..'Z'];
end;

{ Recognize a decimal digit }
function IsDigit(c : char): boolean;
begin
  IsDigit := c in ['0'..'9'];
end;

{ Get an identifier }
function GetName : char;
begin
  if not IsAlpha(Look) then
    Expected('Name');
  GetName := UpCase(Look);
  GetChar;
end;

{ Get a number }
function GetNum: char;
begin
  if not IsDigit(Look) then
    Expected('Integer');
  GetNum := Look;
  GetChar;
end;

{ Output a string with tab }
procedure Emit(s : string);
begin
  Write(TAB, s);
end;

{ Output a string with tab and CRLF }
procedure EmitLn(s : string);
begin
  Emit(s);
  WriteLn;
end;

{ Initialize }
procedure Init;
begin
  GetChar;
end;

{ Parse and translate a maths expression }
procedure Term;
begin
  EmitLn('MOV EAX, ' + GetNum);
end;

{ Recognize and translate an add }
procedure Add;
begin
  Match('+');
  Term;
  EmitLn('ADD EAX, EDX');
end;

{ Recognize and translate a subtract }
procedure Subtract;
begin
  Match('-');
  Term;
  EmitLn('SUB EAX, EDX');
  EmitLn('NEG EAX');
end;
{ Parse and translate an expression }
procedure Expression;
begin
  Term;
  while Look in ['+', '-'] do
    begin
      EmitLn('MOV EDX, EAX');
      case Look of
        '+' : Add;
        '-' : Subtract;
      else
        Expected('Addop');
      end;
    end;
end;

{ Parse and translate an expression }

{ Main Program }
begin
  Init;
  Expression;
  ReadLn;
  WriteLn('Press Enter to Exit');
  ReadLn;
end.
