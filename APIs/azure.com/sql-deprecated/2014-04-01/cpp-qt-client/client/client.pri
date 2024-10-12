QT += network

HEADERS += \
# Models
    $${PWD}/OAIExtensionListResult.h \
    $${PWD}/OAITransparentDataEncryptionListResult.h \
    $${PWD}/OAITransparentDataEncryptionListResult_value_inner.h \
    $${PWD}/OAITransparentDataEncryptionListResult_value_inner_properties.h \
# APIs
    $${PWD}/OAIImportExportApi.h \
    $${PWD}/OAITransparentDataEncryptionApi.h \
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
    $${PWD}/OAIExtensionListResult.cpp \
    $${PWD}/OAITransparentDataEncryptionListResult.cpp \
    $${PWD}/OAITransparentDataEncryptionListResult_value_inner.cpp \
    $${PWD}/OAITransparentDataEncryptionListResult_value_inner_properties.cpp \
# APIs
    $${PWD}/OAIImportExportApi.cpp \
    $${PWD}/OAITransparentDataEncryptionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
