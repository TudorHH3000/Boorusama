import os
import glob

content = (
    "package com.teknorota.flutter_avif\n"
    "import io.flutter.embedding.engine.plugins.FlutterPlugin\n"
    "import io.flutter.plugin.common.MethodCall\n"
    "import io.flutter.plugin.common.MethodChannel\n"
    "import io.flutter.plugin.common.MethodChannel.MethodCallHandler\n"
    "import io.flutter.plugin.common.MethodChannel.Result\n"
    "class FlutterAvifPlugin : FlutterPlugin, MethodCallHandler {\n"
    "  private lateinit var channel: MethodChannel\n"
    "  override fun onAttachedToEngine(binding: FlutterPlugin.FlutterPluginBinding) {\n"
    '    channel = MethodChannel(binding.binaryMessenger, "flutter_avif")\n'
    "    channel.setMethodCallHandler(this)\n"
    "  }\n"
    "  override fun onMethodCall(call: MethodCall, result: Result) {\n"
    "    result.notImplemented()\n"
    "  }\n"
    "  override fun onDetachedFromEngine(binding: FlutterPlugin.FlutterPluginBinding) {\n"
    "    channel.setMethodCallHandler(null)\n"
    "  }\n"
    "}\n"
)

search_dirs = [
    os.path.expanduser("~/.pub-cache"),
    "/home/runner/.pub-cache",
    "/home/runner/work",
]

patched = set()
for search_dir in search_dirs:
    for kt_file in glob.glob(f"{search_dir}/**/FlutterAvifPlugin.kt", recursive=True):
        if kt_file in patched:
            continue
        patched.add(kt_file)
        print(f"Patching {kt_file}")
        with open(kt_file, "w") as f:
            f.write(content)

print("Done")
