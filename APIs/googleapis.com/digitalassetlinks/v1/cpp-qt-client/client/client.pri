QT += network

HEADERS += \
# Models
    $${PWD}/OAIAndroidAppAsset.h \
    $${PWD}/OAIAsset.h \
    $${PWD}/OAIBulkCheckRequest.h \
    $${PWD}/OAIBulkCheckResponse.h \
    $${PWD}/OAICertificateInfo.h \
    $${PWD}/OAICheckResponse.h \
    $${PWD}/OAIListResponse.h \
    $${PWD}/OAIStatement.h \
    $${PWD}/OAIStatementTemplate.h \
    $${PWD}/OAIWebAsset.h \
# APIs
    $${PWD}/OAIAssetlinksApi.h \
    $${PWD}/OAIStatementsApi.h \
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
    $${PWD}/OAIAndroidAppAsset.cpp \
    $${PWD}/OAIAsset.cpp \
    $${PWD}/OAIBulkCheckRequest.cpp \
    $${PWD}/OAIBulkCheckResponse.cpp \
    $${PWD}/OAICertificateInfo.cpp \
    $${PWD}/OAICheckResponse.cpp \
    $${PWD}/OAIListResponse.cpp \
    $${PWD}/OAIStatement.cpp \
    $${PWD}/OAIStatementTemplate.cpp \
    $${PWD}/OAIWebAsset.cpp \
# APIs
    $${PWD}/OAIAssetlinksApi.cpp \
    $${PWD}/OAIStatementsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
