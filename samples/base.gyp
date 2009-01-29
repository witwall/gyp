{
  'settings': {
    'include_dirs': [
      '..',
    ],
  },
  'targets': [
    {
      'name': 'base',
      'type': 'static_library',
      'dependencies': [
        '../third_party/icu38/icu38.gyp:icudata',
        '../third_party/icu38/icu38.gyp:icui18n',
        '../third_party/icu38/icu38.gyp:icuuc',
        '../third_party/libevent/libevent.gyp:libevent',
      ],
      'sources': [
        'third_party/dmg_fp/dtoa.cc',
        'third_party/dmg_fp/g_fmt.cc',
        'third_party/nspr/prtime.cc',
        'third_party/nss/sha512.cc',
        'at_exit.cc',
        'base_paths.cc',
        'base_paths_linux.cc',
        'base_paths_mac.mm',
        'base_paths_win.cc',
        'base_switches.cc',
        'bzip2_error_handler.cc',
        'clipboard.cc',
        'clipboard_linux.cc',
        'clipboard_mac.mm',
        'clipboard_win.cc',
        'command_line.cc',
        'condition_variable_posix.cc',
        'condition_variable_win.cc',
        'debug_util.cc',
        'debug_util_posix.cc',
        'debug_util_win.cc',
        'directory_watcher_win.cc',
        'event_recorder_stubs.cc',
        'field_trial.cc',
        'file_path.cc',
        'file_util.cc',
        'file_util_linux.cc',
        'file_util_mac.mm',
        'file_util_posix.cc',
        'file_util_win.cc',
        'file_version_info_linux.cc',
        'file_version_info_mac.mm',
        'histogram.cc',
        'hmac_mac.cc',
        'hmac_win.cc',
        'icu_util.cc',
        'idle_timer.cc',
        'json_reader.cc',
        'json_writer.cc',
        'lazy_instance.cc',
        'lock.cc',
        'lock_impl_posix.cc',
        'lock_impl_win.cc',
        'logging.cc',
        'mac_util.mm',
        'md5.cc',
        'memory_debug.cc',
        'message_loop.cc',
        'message_pump_default.cc',
        'message_pump_libevent.cc',
        'message_pump_mac.mm',
        'message_pump_win.cc',
        'non_thread_safe.cc',
        'path_service.cc',
        'pickle.cc',
        'platform_file_posix.cc',
        'platform_thread_mac.mm',
        'platform_thread_posix.cc',
        'platform_thread_win.cc',
        'process_posix.cc',
        'process_util_linux.cc',
        'process_util_mac.mm',
        'process_util_posix.cc',
        'process_util_win.cc',
        'rand_util.cc',
        'rand_util_posix.cc',
        'rand_util_win.cc',
        'ref_counted.cc',
        'revocable_store.cc',
        'scoped_bstr_win.cc',
        'scoped_clipboard_writer.cc',
        'scoped_nsautorelease_pool.mm',
        'sha2.cc',
        'shared_memory_posix.cc',
        'shared_memory_win.cc',
        'simple_thread.cc',
        'stats_table.cc',
        'string16.cc',
        'string_escape.cc',
        'string_piece.cc',
        'string_util.cc',
        'string_util_icu.cc',
        'sys_info_posix.cc',
        'sys_info_win.cc',
        'sys_string_conversions_linux.cc',
        'sys_string_conversions_mac.mm',
        'sys_string_conversions_win.cc',
        'system_monitor.cc',
        'system_monitor_posix.cc',
        'system_monitor_win.cc',
        'test_file_util_linux.cc',
        'test_file_util_mac.cc',
        'test_file_util_win.cc',
        'thread.cc',
        'thread_collision_warner.cc',
        'thread_local_posix.cc',
        'thread_local_storage_posix.cc',
        'thread_local_storage_win.cc',
        'thread_local_win.cc',
        'time.cc',
        'time_format.cc',
        'time_mac.cc',
        'time_win.cc',
        'timer.cc',
        'trace_event.cc',
        'tracked.cc',
        'tracked_objects.cc',
        'values.cc',
        'waitable_event_posix.cc',
        'waitable_event_watcher_posix.cc',
        'waitable_event_watcher_win.cc',
        'waitable_event_win.cc',
        'watchdog.cc',
        'word_iterator.cc',
        'worker_pool_mac.mm',
      ],
      'conditions': [
        [ 'OS==win', {
            'source_patterns': [ ['exclude', '_(linux|mac|posix)\\.cc$'],
                                 ['exclude', '\\.mm?$' ],
                               ],
          },
        ],
        [ 'OS==linux', {
            'source_patterns': [ ['exclude', '_(mac|win)\\.cc$'],
                                 ['exclude', '\\.mm?$' ],
                               ],
          },
        ],
        [ 'OS==mac', {
            'source_patterns': [ ['exclude', '_(linux|win)\\.cc$'] ],
            'libraries': [
              '/System/Library/Frameworks/AppKit.framework',
              '/System/Library/Frameworks/Carbon.framework',
              '/System/Library/Frameworks/CoreFoundation.framework',
              '/System/Library/Frameworks/Foundation.framework',
            ],
          },
        ],
      ],
    },
    {
      'name': 'base_unittests',
      'type': 'executable',
      'sources': [
        'at_exit_unittest.cc',
        'atomicops_unittest.cc',
        'clipboard_unittest.cc',
        'command_line_unittest.cc',
        'condition_variable_unittest.cc',
        'field_trial_unittest.cc',
        'file_path_unittest.cc',
        'file_util_unittest.cc',
        'file_version_info_unittest.cc',
        'histogram_unittest.cc',
        'hmac_unittest.cc',
        'idletimer_unittest.cc',
        'json_reader_unittest.cc',
        'json_writer_unittest.cc',
        'lazy_instance_unittest.cc',
        'linked_ptr_unittest.cc',
        'mac_util_unittest.cc',
        'message_loop_unittest.cc',
        'observer_list_unittest.cc',
        'path_service_unittest.cc',
        'pickle_unittest.cc',
        'process_util_unittest.cc',
        'pr_time_unittest.cc',
        'rand_util_unittest.cc',
        'ref_counted_unittest.cc',
        'run_all_unittests.cc',
        'scoped_ptr_unittest.cc',
        'sha2_unittest.cc',
        'shared_memory_unittest.cc',
        'simple_thread_unittest.cc',
        'singleton_unittest.cc',
        'stack_container_unittest.cc',
        'string_escape_unittest.cc',
        'string_piece_unittest.cc',
        'string_tokenizer_unittest.cc',
        'string_util_unittest.cc',
        'sys_info_unittest.cc',
        'sys_string_conversions_unittest.cc',
        'thread_collision_warner_unittest.cc',
        'thread_local_storage_unittest.cc',
        'thread_local_unittest.cc',
        'thread_unittest.cc',
        'time_unittest.cc',
        'timer_unittest.cc',
        'tracked_objects_unittest.cc',
        'tuple_unittest.cc',
        'values_unittest.cc',
        'waitable_event_unittest.cc',
        'watchdog_unittest.cc',
        'word_iterator_unittest.cc',
        'worker_pool_unittest.cc',
      ],
      'include_dirs': [
        # word_iterator.h (used by word_iterator_unittest.cc) leaks an ICU
        # #include for unicode/uchar.h.  This should probably be cleaned up.
        '../third_party/icu38/public/common',
      ],
      'dependencies': [
        'base',
        '../testing/gtest.gyp:gtest',
      ],
    },
  ],
}
