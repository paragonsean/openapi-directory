QT += network

HEADERS += \
# Models
    $${PWD}/OAILatLng.h \
    $${PWD}/OAIResponse.h \
    $${PWD}/OAIResponse_licenses_inner.h \
    $${PWD}/OAIResponse_rate.h \
    $${PWD}/OAIResponse_results_inner.h \
    $${PWD}/OAIResponse_results_inner_bounds.h \
    $${PWD}/OAIResponse_status.h \
    $${PWD}/OAIResponse_stay_informed.h \
    $${PWD}/OAIResponse_timestamp.h \
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
    $${PWD}/OAILatLng.cpp \
    $${PWD}/OAIResponse.cpp \
    $${PWD}/OAIResponse_licenses_inner.cpp \
    $${PWD}/OAIResponse_rate.cpp \
    $${PWD}/OAIResponse_results_inner.cpp \
    $${PWD}/OAIResponse_results_inner_bounds.cpp \
    $${PWD}/OAIResponse_status.cpp \
    $${PWD}/OAIResponse_stay_informed.cpp \
    $${PWD}/OAIResponse_timestamp.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
