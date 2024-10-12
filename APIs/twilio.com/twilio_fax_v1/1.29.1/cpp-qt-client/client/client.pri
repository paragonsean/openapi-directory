QT += network

HEADERS += \
# Models
    $${PWD}/OAIFax_v1_fax.h \
    $${PWD}/OAIFax_v1_fax_fax_media.h \
    $${PWD}/OAIListFaxMediaResponse.h \
    $${PWD}/OAIListFaxResponse.h \
    $${PWD}/OAIListFaxResponse_meta.h \
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
    $${PWD}/OAIFax_v1_fax.cpp \
    $${PWD}/OAIFax_v1_fax_fax_media.cpp \
    $${PWD}/OAIListFaxMediaResponse.cpp \
    $${PWD}/OAIListFaxResponse.cpp \
    $${PWD}/OAIListFaxResponse_meta.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
