/**
 * Story
 * This API is the main entry point for creating, editing and publishing analytics throught the Presalytics API
 *
 * The version of the OpenAPI document: 0.3.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIStory.h
 *
 * Model for story objects
 */

#ifndef OAIStory_H
#define OAIStory_H

#include <QJsonObject>

#include "OAIOoxml_document.h"
#include "OAIStory_collaborator.h"
#include "OAIStory_outline_history.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIStory_collaborator;
class OAIOoxml_document;
class OAIStory_outline_history;

class OAIStory : public OAIObject {
public:
    OAIStory();
    OAIStory(QString json);
    ~OAIStory() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getCreatedAt() const;
    void setCreatedAt(const QDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getCreatedBy() const;
    void setCreatedBy(const QString &created_by);
    bool is_created_by_Set() const;
    bool is_created_by_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QDateTime getUpdatedAt() const;
    void setUpdatedAt(const QDateTime &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    QString getUpdatedBy() const;
    void setUpdatedBy(const QString &updated_by);
    bool is_updated_by_Set() const;
    bool is_updated_by_Valid() const;

    QList<OAIStory_collaborator> getCollaborators() const;
    void setCollaborators(const QList<OAIStory_collaborator> &collaborators);
    bool is_collaborators_Set() const;
    bool is_collaborators_Valid() const;

    bool isIsPublic() const;
    void setIsPublic(const bool &is_public);
    bool is_is_public_Set() const;
    bool is_is_public_Valid() const;

    QList<OAIOoxml_document> getOoxmlDocuments() const;
    void setOoxmlDocuments(const QList<OAIOoxml_document> &ooxml_documents);
    bool is_ooxml_documents_Set() const;
    bool is_ooxml_documents_Valid() const;

    QString getOutline() const;
    void setOutline(const QString &outline);
    bool is_outline_Set() const;
    bool is_outline_Valid() const;

    QList<OAIStory_outline_history> getOutlineHistory() const;
    void setOutlineHistory(const QList<OAIStory_outline_history> &outline_history);
    bool is_outline_history_Set() const;
    bool is_outline_history_Valid() const;

    qint32 getRevision() const;
    void setRevision(const qint32 &revision);
    bool is_revision_Set() const;
    bool is_revision_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_created_by;
    bool m_created_by_isSet;
    bool m_created_by_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QDateTime m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;

    QString m_updated_by;
    bool m_updated_by_isSet;
    bool m_updated_by_isValid;

    QList<OAIStory_collaborator> m_collaborators;
    bool m_collaborators_isSet;
    bool m_collaborators_isValid;

    bool m_is_public;
    bool m_is_public_isSet;
    bool m_is_public_isValid;

    QList<OAIOoxml_document> m_ooxml_documents;
    bool m_ooxml_documents_isSet;
    bool m_ooxml_documents_isValid;

    QString m_outline;
    bool m_outline_isSet;
    bool m_outline_isValid;

    QList<OAIStory_outline_history> m_outline_history;
    bool m_outline_history_isSet;
    bool m_outline_history_isValid;

    qint32 m_revision;
    bool m_revision_isSet;
    bool m_revision_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStory)

#endif // OAIStory_H
