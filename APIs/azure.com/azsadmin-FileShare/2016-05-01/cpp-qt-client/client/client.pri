QT += network

HEADERS += \
# Models
    $${PWD}/OAIFileShare.h \
    $${PWD}/OAIFileShareList.h \
    $${PWD}/OAIFileShareModel.h \
# APIs
    $${PWD}/OAIFileSharesApi.h \
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
    $${PWD}/OAIFileShare.cpp \
    $${PWD}/OAIFileShareList.cpp \
    $${PWD}/OAIFileShareModel.cpp \
# APIs
    $${PWD}/OAIFileSharesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
