import QtQuick
import QtQuick.Controls.Material

ApplicationWindow {
    visible: true
    width: 360
    height: 640
    title: "Hello Qt"
    
    // Default Material You Design
    Material.theme: Material.Dark
    Material.accent: Material.LightBlue

    Column {
        anchors.centerIn: parent
        spacing: 25

        Text {
            id: statusText
            text: "Waiting for Python..."
            color: "white"
            font.pixelSize: 22
            font.bold: true
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Button {
            text: "TEST PYTHON ENGINE"
            anchors.horizontalCenter: parent.horizontalCenter
            
            // Jab button click hoga, Python ka function call hoga!
            onClicked: {
                statusText.text = backend.process_text("Akash")
                statusText.color = "#00FF00" // Text green ho jayega
            }
        }
    }
}
