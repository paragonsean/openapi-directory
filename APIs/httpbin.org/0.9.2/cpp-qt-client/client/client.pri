QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIAnythingApi.h \
    $${PWD}/OAIAuthApi.h \
    $${PWD}/OAICookiesApi.h \
    $${PWD}/OAIDynamicDataApi.h \
    $${PWD}/OAIHTTPMethodsApi.h \
    $${PWD}/OAIImagesApi.h \
    $${PWD}/OAIRedirectsApi.h \
    $${PWD}/OAIRequestInspectionApi.h \
    $${PWD}/OAIResponseFormatsApi.h \
    $${PWD}/OAIResponseInspectionApi.h \
    $${PWD}/OAIStatusCodesApi.h \
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
# APIs
    $${PWD}/OAIAnythingApi.cpp \
    $${PWD}/OAIAuthApi.cpp \
    $${PWD}/OAICookiesApi.cpp \
    $${PWD}/OAIDynamicDataApi.cpp \
    $${PWD}/OAIHTTPMethodsApi.cpp \
    $${PWD}/OAIImagesApi.cpp \
    $${PWD}/OAIRedirectsApi.cpp \
    $${PWD}/OAIRequestInspectionApi.cpp \
    $${PWD}/OAIResponseFormatsApi.cpp \
    $${PWD}/OAIResponseInspectionApi.cpp \
    $${PWD}/OAIStatusCodesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
