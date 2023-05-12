/* notes:
# how to use
  > build the exe   
  > open csgo in -insecure   
  > run the exe   
  > reads out values   
  > input your sensitivity   
  > read, add, profit ???   
## to update
  > update pitchclassptr, yawclassptr, and sensclassptr
  > from hazedumper @ https://github.com/frk1/hazedumper/blob/master/csgo.hpp   
## to reset   
  > set m_pitch and m_yaw in console to 0.0220 :) will add a reset functionality for this later shhhhh   
*/

#include <iostream>
#define WIN32_LEAN_AND_MEAN
#include <Windows.h>
#include <TlHelp32.h>

int main( ) {
  // get game info
  unsigned int pid{ };
  void*        phandle{ };
  while( !pid ) {
    PROCESSENTRY32 e{ };
    e.dwSize = sizeof( e );
    const HANDLE snap = CreateToolhelp32Snapshot( TH32CS_SNAPPROCESS, 0 );
    while( Process32Next( snap, &e ) ) {
      if( !wcscmp( L"csgo.exe", e.szExeFile ) ) {
        pid = e.th32ProcessID;
        phandle = OpenProcess( PROCESS_ALL_ACCESS, 0, ( unsigned long )pid );
        std::cout << "found the game\n";
        break;
      }
    }
    if( snap ) CloseHandle( snap );
  }

  // get client dll
  MODULEENTRY32 e{ };
  e.dwSize = sizeof( e );
  unsigned int client{ };
  const auto snap = CreateToolhelp32Snapshot( TH32CS_SNAPMODULE, ( unsigned long )pid );
  while( Module32Next( snap, &e ) ) {
    if( !wcscmp( L"client.dll", e.szModule ) ) {
      client = reinterpret_cast< unsigned int >( e.modBaseAddr );
      std::cout << "found client.dll\n";
      break;
    }
  }
  // global vars
  unsigned int value{ };

  // m_pitch
  float set_pitch = 0.044f;
  unsigned int pitchclassptr = client + 0x5238038;
  std::cout << "pitch | value:index" << std::endl;
  for( unsigned int i = 0; i < 0x128; i++ ) {
    unsigned int val{ };
    ReadProcessMemory( phandle, reinterpret_cast< const void* >( pitchclassptr + i ), &val, sizeof( unsigned int ), 0 );
    val = val ^ pitchclassptr;
    if( *( float* )( &val ) == 0.022f ) {
      std::cout << *( float* )( &val ) << ":" << i << std::endl;
      unsigned int pitch_xor = ( *reinterpret_cast< unsigned int* >( &set_pitch ) ^ ( pitchclassptr + i ) );
      WriteProcessMemory( phandle, reinterpret_cast< void* >( pitchclassptr + i ), &pitch_xor, sizeof( float ), NULL );
      break;
    }
  }

  Sleep( 500 );

  // m_yaw
  float set_yaw = 0.044f;
  unsigned int yawclassptr = client + 0xDED928;
  std::cout << "yaw   | value:index" << std::endl;
  for( unsigned int i = 0; i < 0x128; i++ ) {
    unsigned int val{ };
    ReadProcessMemory( phandle, reinterpret_cast< const void* >( yawclassptr + i ), &val, sizeof( unsigned int ), 0 );
    val = val ^ yawclassptr;
    if( *( float* )( &val ) == 0.022f ) {
      std::cout << *( float* )( &val ) << ":" << i << std::endl;
      unsigned int yaw_xor = ( *reinterpret_cast< unsigned int* >( &set_yaw ) ^ ( yawclassptr + i ) );
      WriteProcessMemory( phandle, reinterpret_cast< void* >( yawclassptr + i ), &yaw_xor, sizeof( float ), NULL );
      break;
    }
  }

  // sensitivity
  std::cout << "your sens : ";
  float sens_in;
  std::cin >> sens_in;
  unsigned int sensclassptr = client + 0xDEDB98;
  std::cout << "sens  | value:index" << std::endl;
  for( unsigned int i = 0; i < 0x128; i++ ) {
    unsigned int val{ };
    ReadProcessMemory( phandle, reinterpret_cast< const void* >( sensclassptr + i ), &val, sizeof( unsigned int ), 0 );
    val = val ^ sensclassptr;
    if( *( float* )( &val ) == sens_in ) {
      std::cout << *( float* )( &val ) << ":" << i << std::endl;
    }
  }
  

  while( true ) {
  
  }

  return 0;
}
