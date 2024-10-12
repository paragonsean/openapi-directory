QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddressDataDto.h \
    $${PWD}/OAICartItemDto.h \
    $${PWD}/OAIInvoiceInformationDto.h \
    $${PWD}/OAILinkCreateRequest.h \
    $${PWD}/OAILinkResponse.h \
    $${PWD}/OAIPageLinkResponse.h \
    $${PWD}/OAIPageable.h \
    $${PWD}/OAISort.h \
# APIs
    $${PWD}/OAILinkManagementApi.h \
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
    $${PWD}/OAIAddressDataDto.cpp \
    $${PWD}/OAICartItemDto.cpp \
    $${PWD}/OAIInvoiceInformationDto.cpp \
    $${PWD}/OAILinkCreateRequest.cpp \
    $${PWD}/OAILinkResponse.cpp \
    $${PWD}/OAIPageLinkResponse.cpp \
    $${PWD}/OAIPageable.cpp \
    $${PWD}/OAISort.cpp \
# APIs
    $${PWD}/OAILinkManagementApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
