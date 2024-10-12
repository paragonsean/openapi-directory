QT += network

HEADERS += \
# Models
    $${PWD}/OAIExportRequest.h \
    $${PWD}/OAIImportExportResponse.h \
    $${PWD}/OAIImportExportResponseProperties.h \
    $${PWD}/OAIImportExtensionProperties.h \
    $${PWD}/OAIImportExtensionRequest.h \
    $${PWD}/OAIImportRequest.h \
# APIs
    $${PWD}/OAIImportExportApi.h \
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
    $${PWD}/OAIExportRequest.cpp \
    $${PWD}/OAIImportExportResponse.cpp \
    $${PWD}/OAIImportExportResponseProperties.cpp \
    $${PWD}/OAIImportExtensionProperties.cpp \
    $${PWD}/OAIImportExtensionRequest.cpp \
    $${PWD}/OAIImportRequest.cpp \
# APIs
    $${PWD}/OAIImportExportApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
