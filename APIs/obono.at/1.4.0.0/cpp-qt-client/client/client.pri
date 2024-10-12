QT += network

HEADERS += \
# Models
    $${PWD}/OAIAbschlussbelegdaten.h \
    $${PWD}/OAIAuthResult.h \
    $${PWD}/OAIBeleg.h \
    $${PWD}/OAIBelegdaten.h \
    $${PWD}/OAIBelege.h \
    $${PWD}/OAIBelegformat.h \
    $${PWD}/OAIExportformat.h \
    $${PWD}/OAIExportformat_Belege_Gruppe_inner.h \
    $${PWD}/OAIMonatsbeleg.h \
    $${PWD}/OAIPosten.h \
    $${PWD}/OAIRabatt.h \
    $${PWD}/OAIRegistrierkasse.h \
    $${PWD}/OAISignierteBelegdaten.h \
    $${PWD}/OAIZahlung.h \
# APIs
    $${PWD}/OAIAuthApi.h \
    $${PWD}/OAIBelegApi.h \
    $${PWD}/OAIExportApi.h \
    $${PWD}/OAIMonatsbelegeApi.h \
    $${PWD}/OAIRegistrierkasseApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIAbschlussbelegdaten.cpp \
    $${PWD}/OAIAuthResult.cpp \
    $${PWD}/OAIBeleg.cpp \
    $${PWD}/OAIBelegdaten.cpp \
    $${PWD}/OAIBelege.cpp \
    $${PWD}/OAIBelegformat.cpp \
    $${PWD}/OAIExportformat.cpp \
    $${PWD}/OAIExportformat_Belege_Gruppe_inner.cpp \
    $${PWD}/OAIMonatsbeleg.cpp \
    $${PWD}/OAIPosten.cpp \
    $${PWD}/OAIRabatt.cpp \
    $${PWD}/OAIRegistrierkasse.cpp \
    $${PWD}/OAISignierteBelegdaten.cpp \
    $${PWD}/OAIZahlung.cpp \
# APIs
    $${PWD}/OAIAuthApi.cpp \
    $${PWD}/OAIBelegApi.cpp \
    $${PWD}/OAIExportApi.cpp \
    $${PWD}/OAIMonatsbelegeApi.cpp \
    $${PWD}/OAIRegistrierkasseApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
