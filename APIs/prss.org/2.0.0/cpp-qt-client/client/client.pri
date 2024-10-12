QT += network

HEADERS += \
# Models
    $${PWD}/OAIBroadcastService.h \
    $${PWD}/OAICDDriveFile.h \
    $${PWD}/OAICDDriveFolder.h \
    $${PWD}/OAICDDriveItem.h \
    $${PWD}/OAIEpisode.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIPiece.h \
    $${PWD}/OAIProgram.h \
    $${PWD}/OAIProgramInformationBatch.h \
    $${PWD}/OAIProgramInformationBatch_program.h \
    $${PWD}/OAISegment.h \
    $${PWD}/OAISpot.h \
    $${PWD}/OAISpotInsertion.h \
    $${PWD}/OAI_api_v2_cddrive_folders__folder_id__items_get_200_response.h \
    $${PWD}/OAI_api_v2_metapub_program_information_batch_post_request.h \
    $${PWD}/OAI_api_v2_metapub_program_information_batch_post_request_program.h \
# APIs
    $${PWD}/OAIBroadcastServicesApi.h \
    $${PWD}/OAICDDriveApi.h \
    $${PWD}/OAIEpisodesApi.h \
    $${PWD}/OAIMetaPubApi.h \
    $${PWD}/OAIPiecesApi.h \
    $${PWD}/OAIProgramsApi.h \
    $${PWD}/OAIRadioDNSApi.h \
    $${PWD}/OAISegmentsApi.h \
    $${PWD}/OAISpotInsertionsApi.h \
    $${PWD}/OAISpotsApi.h \
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
    $${PWD}/OAIBroadcastService.cpp \
    $${PWD}/OAICDDriveFile.cpp \
    $${PWD}/OAICDDriveFolder.cpp \
    $${PWD}/OAICDDriveItem.cpp \
    $${PWD}/OAIEpisode.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIPiece.cpp \
    $${PWD}/OAIProgram.cpp \
    $${PWD}/OAIProgramInformationBatch.cpp \
    $${PWD}/OAIProgramInformationBatch_program.cpp \
    $${PWD}/OAISegment.cpp \
    $${PWD}/OAISpot.cpp \
    $${PWD}/OAISpotInsertion.cpp \
    $${PWD}/OAI_api_v2_cddrive_folders__folder_id__items_get_200_response.cpp \
    $${PWD}/OAI_api_v2_metapub_program_information_batch_post_request.cpp \
    $${PWD}/OAI_api_v2_metapub_program_information_batch_post_request_program.cpp \
# APIs
    $${PWD}/OAIBroadcastServicesApi.cpp \
    $${PWD}/OAICDDriveApi.cpp \
    $${PWD}/OAIEpisodesApi.cpp \
    $${PWD}/OAIMetaPubApi.cpp \
    $${PWD}/OAIPiecesApi.cpp \
    $${PWD}/OAIProgramsApi.cpp \
    $${PWD}/OAIRadioDNSApi.cpp \
    $${PWD}/OAISegmentsApi.cpp \
    $${PWD}/OAISpotInsertionsApi.cpp \
    $${PWD}/OAISpotsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
