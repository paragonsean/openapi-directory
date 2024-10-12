QT += network

HEADERS += \
# Models
    $${PWD}/OAIBrowserJsonResponse.h \
    $${PWD}/OAIInfoResponse.h \
    $${PWD}/OAIInputImage.h \
    $${PWD}/OAISearchData.h \
    $${PWD}/OAISearchItem.h \
    $${PWD}/OAISearch_Results.h \
# APIs
    $${PWD}/OAIFaceCheckAPIApi.h \
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
    $${PWD}/OAIBrowserJsonResponse.cpp \
    $${PWD}/OAIInfoResponse.cpp \
    $${PWD}/OAIInputImage.cpp \
    $${PWD}/OAISearchData.cpp \
    $${PWD}/OAISearchItem.cpp \
    $${PWD}/OAISearch_Results.cpp \
# APIs
    $${PWD}/OAIFaceCheckAPIApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
