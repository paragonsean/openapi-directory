QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiResponsError.h \
    $${PWD}/OAIApps.h \
    $${PWD}/OAIDataRaw.h \
    $${PWD}/OAIDataTabular.h \
    $${PWD}/OAIDataTabular_data.h \
    $${PWD}/OAIGeoCoordinates.h \
    $${PWD}/OAISocialMedia.h \
    $${PWD}/OAIUrl.h \
    $${PWD}/OAIUrlBrowser.h \
    $${PWD}/OAIUrl_additionalData.h \
    $${PWD}/OAIUrl_additionalData_locality.h \
    $${PWD}/OAIUrl_items_inner.h \
# APIs
    $${PWD}/OAIRESTEndpointsApi.h \
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
    $${PWD}/OAIApiResponsError.cpp \
    $${PWD}/OAIApps.cpp \
    $${PWD}/OAIDataRaw.cpp \
    $${PWD}/OAIDataTabular.cpp \
    $${PWD}/OAIDataTabular_data.cpp \
    $${PWD}/OAIGeoCoordinates.cpp \
    $${PWD}/OAISocialMedia.cpp \
    $${PWD}/OAIUrl.cpp \
    $${PWD}/OAIUrlBrowser.cpp \
    $${PWD}/OAIUrl_additionalData.cpp \
    $${PWD}/OAIUrl_additionalData_locality.cpp \
    $${PWD}/OAIUrl_items_inner.cpp \
# APIs
    $${PWD}/OAIRESTEndpointsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
