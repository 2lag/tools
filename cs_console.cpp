#include <iostream>
#include <string>
#include <Windows.h>

int main( ) {
  char cmd[ 512 ];
  std::string input;
  
  const HWND game_console = FindWindowA( "Valve001", 0 );

  if( !game_console )
    return 1;

  COPYDATASTRUCT cmd_data;

  while( true ) {
    std::cout << "cmd: ";
    std::getline( std::cin, input );
    strcpy_s( cmd, sizeof( cmd ), input.c_str( ) );
    cmd_data.cbData = strlen( cmd ) + 1;
    cmd_data.dwData = 0;
    cmd_data.lpData = ( void* )cmd;

    SendMessageA( game_console, WM_COPYDATA, 0, ( LPARAM )&cmd_data );

    Sleep( 1000 );
  }

  return 0;
}
