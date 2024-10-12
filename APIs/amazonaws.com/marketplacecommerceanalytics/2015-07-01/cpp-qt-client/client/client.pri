QT += network

HEADERS += \
# Models
    $${PWD}/OAIDataSetType.h \
    $${PWD}/OAIGenerateDataSetRequest.h \
    $${PWD}/OAIGenerateDataSetResult.h \
    $${PWD}/OAIStartSupportDataExportRequest.h \
    $${PWD}/OAIStartSupportDataExportResult.h \
    $${PWD}/OAISupportDataSetType.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIDataSetType.cpp \
    $${PWD}/OAIGenerateDataSetRequest.cpp \
    $${PWD}/OAIGenerateDataSetResult.cpp \
    $${PWD}/OAIStartSupportDataExportRequest.cpp \
    $${PWD}/OAIStartSupportDataExportResult.cpp \
    $${PWD}/OAISupportDataSetType.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
