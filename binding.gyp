{
    "targets": [
    {

        "target_name": "yaz0",
        "sources": [
            "src/main.cpp",
                "src/yaz0/chunk.cpp",
                "src/yaz0/base.cpp",
                "src/yaz0/parser.cpp",
                "src/yaz0/creator.cpp"
        ],
        "cflags": [
          "-std=c++11",
          '-O3'
        ],
        "cflags": [ "-fexceptions" ],
        "cflags": [ "-fno-exceptions" ],
        "cflags_cc": [ "-fexceptions" ],
        "cflags_cc": [ "-fno-exceptions" ],
        'conditions': [
            ['OS=="mac"', {
                'xcode_settings': {
                    'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
                }
            }]
        ]
    }
    ]
}
