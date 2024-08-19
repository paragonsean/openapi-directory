QT += network

HEADERS += \
# Models
    $${PWD}/OAIAPI_Key_Info.h \
    $${PWD}/OAIDomains.h \
    $${PWD}/OAIMX_records.h \
    $${PWD}/OAIResponse_Parameters.h \
    $${PWD}/OAISearch_Results.h \
    $${PWD}/OAIUpdate_model.h \
    $${PWD}/OAIZone_info.h \
    $${PWD}/OAIZone_statistics.h \
    $${PWD}/OAIZone_stats.h \
# APIs
    $${PWD}/OAIDomainsApi.h \
    $${PWD}/OAIInfoApi.h \
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
    $${PWD}/OAIAPI_Key_Info.cpp \
    $${PWD}/OAIDomains.cpp \
    $${PWD}/OAIMX_records.cpp \
    $${PWD}/OAIResponse_Parameters.cpp \
    $${PWD}/OAISearch_Results.cpp \
    $${PWD}/OAIUpdate_model.cpp \
    $${PWD}/OAIZone_info.cpp \
    $${PWD}/OAIZone_statistics.cpp \
    $${PWD}/OAIZone_stats.cpp \
# APIs
    $${PWD}/OAIDomainsApi.cpp \
    $${PWD}/OAIInfoApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
