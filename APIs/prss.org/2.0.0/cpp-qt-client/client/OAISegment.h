/**
 * ContentDepot
 * ContentDepot hosts a range of API’s that allow clients to manage, discover, and obtain content. The API spans many parts of the ContentDepot functionality including MetaPub (a.k.a. metadata distribution) and content management.  ## MetaPub  MetaPub collects, normalizes and distributes publicly available program, episode, and piece metadata through the public radio system. Backed by ContentDepot and its data model, MetaPub allows producers to supply metadata through various methods:  1. MetaPub Agents that collect producer metadata by \"crawling\" existing public feeds (e.g. C24, BBC) or the producer's production system (e.g. ATC, ME, TED Radio Hour). 2. Manually enter metadata in the ContentDepot Portal on each program and episode. 3. Publish/push the metadata to the MetaPub upload API and execute an ingest job.  MetaPub then distributes this data to stations through an electronic program guide (EPG model) for display on various listener devices such as smart phones, tablets, web streams, HD radios, RDBS enabled FM radios, and more. The EPG format is based on the RadioDNS specifications.  ### RadioDNS  The RadioDNS Service and Programme Information Specification ([ETSI TS 102 818 v3.4.1](https://www.etsi.org/deliver/etsi_ts/102800_102899/102818/03.04.01_60/ts_102818v030401p.pdf)) defines three primary documents: Service Information, Program Information, and Group Information. These documents, along with the core RadioDNS Hybrid Lookup for Radio Services Specification ([ETSI TS 103 270 v1.4.1](https://www.etsi.org/deliver/etsi_ts/103200_103299/103270/01.04.01_60/ts_103270v010401p.pdf)), define a system where an end listener device can dynamically discover program metadata and fetch the metadata via Internet Protocol (IP) requests. MetaPub's use of RadioDNS differs slightly in that MetaPub (a.k.a PRSS) acts as the \"service provider\" while the stations and related middleware act as the end devices. While this is not the primary use case of RadioDNS, the flexibility in the specification, service definitions, and DNS resolution allows this model to be easily represented. MetaPub provides both _National Metadata_ and _Station Metadata_.  It is strongly recommended that the related [RadioDNS specifications](https://radiodns.org/developers/documentation/) be read for implementation details, definitions, and required XML schemas.  ## ContentDepot Drive  ContentDepot Drive (CD Drive) provides a private, per customer file storage solution similar to other cloud storage solutions such as Google Drive, Box, and Dropbox. The CD Drive is used to stage content uploads such as metadata files, images, or segment audio before associating the content with specific programs or episodes.  CD Drive content can be referenced using a URI by some operations such as synchronizing metadata. There are two possible CD Drive URI formats supported: ID and hierarchical path. The ID reference takes the form ```cddrive:id:{value}``` where value is the integer ID of the file or folder being referenced. The hierarchical path reference takes the form ```cddrive://{path}``` where path is the full, UNIX style path to the file or folder starting with '/'. For example, two CD Drive URIs pointing to the same file may be ```cddrive:id:12345``` and ```cddrive:///show1/episode2/metadata.xml```. More information about URIs can be found at [Wikipedia](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier).  ## Authentication  The API currently uses OAuth 2.0.  All operations require ```cd:full``` access where the client access is only limited by the permissions of the ContentDepot user after authentication. Limiting access scope per client is not currently supported. 
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISegment.h
 *
 * An audio segment in an episode.
 */

#ifndef OAISegment_H
#define OAISegment_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISegment : public OAIObject {
public:
    OAISegment();
    OAISegment(QString json);
    ~OAISegment() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getChannels() const;
    void setChannels(const qint32 &channels);
    bool is_channels_Set() const;
    bool is_channels_Valid() const;

    QDateTime getCreatedDate() const;
    void setCreatedDate(const QDateTime &created_date);
    bool is_created_date_Set() const;
    bool is_created_date_Valid() const;

    qint64 getEpisodeId() const;
    void setEpisodeId(const qint64 &episode_id);
    bool is_episode_id_Set() const;
    bool is_episode_id_Valid() const;

    QString getFileName() const;
    void setFileName(const QString &file_name);
    bool is_file_name_Set() const;
    bool is_file_name_Valid() const;

    qint64 getFileSize() const;
    void setFileSize(const qint64 &file_size);
    bool is_file_size_Set() const;
    bool is_file_size_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getInCue() const;
    void setInCue(const QString &in_cue);
    bool is_in_cue_Set() const;
    bool is_in_cue_Valid() const;

    QDateTime getLastModifiedDate() const;
    void setLastModifiedDate(const QDateTime &last_modified_date);
    bool is_last_modified_date_Set() const;
    bool is_last_modified_date_Valid() const;

    qint32 getLength() const;
    void setLength(const qint32 &length);
    bool is_length_Set() const;
    bool is_length_Valid() const;

    QString getOriginalFileName() const;
    void setOriginalFileName(const QString &original_file_name);
    bool is_original_file_name_Set() const;
    bool is_original_file_name_Valid() const;

    QString getOutCue() const;
    void setOutCue(const QString &out_cue);
    bool is_out_cue_Set() const;
    bool is_out_cue_Valid() const;

    qint32 getSegmentNumber() const;
    void setSegmentNumber(const qint32 &segment_number);
    bool is_segment_number_Set() const;
    bool is_segment_number_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_channels;
    bool m_channels_isSet;
    bool m_channels_isValid;

    QDateTime m_created_date;
    bool m_created_date_isSet;
    bool m_created_date_isValid;

    qint64 m_episode_id;
    bool m_episode_id_isSet;
    bool m_episode_id_isValid;

    QString m_file_name;
    bool m_file_name_isSet;
    bool m_file_name_isValid;

    qint64 m_file_size;
    bool m_file_size_isSet;
    bool m_file_size_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_in_cue;
    bool m_in_cue_isSet;
    bool m_in_cue_isValid;

    QDateTime m_last_modified_date;
    bool m_last_modified_date_isSet;
    bool m_last_modified_date_isValid;

    qint32 m_length;
    bool m_length_isSet;
    bool m_length_isValid;

    QString m_original_file_name;
    bool m_original_file_name_isSet;
    bool m_original_file_name_isValid;

    QString m_out_cue;
    bool m_out_cue_isSet;
    bool m_out_cue_isValid;

    qint32 m_segment_number;
    bool m_segment_number_isSet;
    bool m_segment_number_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISegment)

#endif // OAISegment_H
