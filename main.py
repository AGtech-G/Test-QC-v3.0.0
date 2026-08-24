import sys
import os
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot

# Ye Backend class C++ aur QML ke sath direct baat karegi!
class Backend(QObject):
    @Slot(str, result=str)
    def process_text(self, text):
        print(f"Python received: {text}")
        return f"Hello {text}, Python is working at C-Speed! 🚀"

if __name__ == "__main__":
    # 1. Initialize Qt Engine
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # 2. Python Backend ko QML me pass karo
    backend = Backend()
    engine.rootContext().setContextProperty("backend", backend)

    # 3. QML UI file load karo
    qml_file = os.path.join(os.path.dirname(__file__), "Main.qml")
    engine.load(qml_file)

    if not engine.rootObjects():
        sys.exit(-1)
        
    sys.exit(app.exec())
