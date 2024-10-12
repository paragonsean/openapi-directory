QT += network

HEADERS += \
# Models
    $${PWD}/OAI_api_v2_0__database__assemblies__barcode__get_request.h \
    $${PWD}/OAI_api_v2_0__database__schemes__barcode__get_request.h \
    $${PWD}/OAI_api_v2_0__database__strains__barcode__get_request.h \
    $${PWD}/OAI_api_v2_0__database__traces__barcode__get_request.h \
    $${PWD}/OAI_api_v2_0_lookup__barcode__post_request.h \
# APIs
    $${PWD}/OAIAllelesApi.h \
    $${PWD}/OAIAssembliesApi.h \
    $${PWD}/OAIInfoApi.h \
    $${PWD}/OAILociApi.h \
    $${PWD}/OAILoginApi.h \
    $${PWD}/OAILookupApi.h \
    $${PWD}/OAISchemesApi.h \
    $${PWD}/OAIStraindataApi.h \
    $${PWD}/OAIStrainsApi.h \
    $${PWD}/OAIStrainsversionApi.h \
    $${PWD}/OAIStsApi.h \
    $${PWD}/OAITracesApi.h \
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
    $${PWD}/OAI_api_v2_0__database__assemblies__barcode__get_request.cpp \
    $${PWD}/OAI_api_v2_0__database__schemes__barcode__get_request.cpp \
    $${PWD}/OAI_api_v2_0__database__strains__barcode__get_request.cpp \
    $${PWD}/OAI_api_v2_0__database__traces__barcode__get_request.cpp \
    $${PWD}/OAI_api_v2_0_lookup__barcode__post_request.cpp \
# APIs
    $${PWD}/OAIAllelesApi.cpp \
    $${PWD}/OAIAssembliesApi.cpp \
    $${PWD}/OAIInfoApi.cpp \
    $${PWD}/OAILociApi.cpp \
    $${PWD}/OAILoginApi.cpp \
    $${PWD}/OAILookupApi.cpp \
    $${PWD}/OAISchemesApi.cpp \
    $${PWD}/OAIStraindataApi.cpp \
    $${PWD}/OAIStrainsApi.cpp \
    $${PWD}/OAIStrainsversionApi.cpp \
    $${PWD}/OAIStsApi.cpp \
    $${PWD}/OAITracesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
