QT += network

HEADERS += \
# Models
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudErrorBody.h \
    $${PWD}/OAIFileServiceItems.h \
    $${PWD}/OAIFileServiceProperties.h \
    $${PWD}/OAIFileShare.h \
    $${PWD}/OAIFileShareItem.h \
    $${PWD}/OAIFileShareItems.h \
    $${PWD}/OAIFileShareProperties.h \
# APIs
    $${PWD}/OAIFileServiceApi.h \
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
    $${PWD}/OAICloudError.cpp \
    $${PWD}/OAICloudErrorBody.cpp \
    $${PWD}/OAIFileServiceItems.cpp \
    $${PWD}/OAIFileServiceProperties.cpp \
    $${PWD}/OAIFileShare.cpp \
    $${PWD}/OAIFileShareItem.cpp \
    $${PWD}/OAIFileShareItems.cpp \
    $${PWD}/OAIFileShareProperties.cpp \
# APIs
    $${PWD}/OAIFileServiceApi.cpp \
    $${PWD}/OAIFileSharesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
