/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIImageSummary.h
 *
 * ImageSummary image summary
 */

#ifndef OAIImageSummary_H
#define OAIImageSummary_H

#include <QJsonObject>

#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIImageSummary : public OAIObject {
public:
    OAIImageSummary();
    OAIImageSummary(QString json);
    ~OAIImageSummary() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getContainers() const;
    void setContainers(const qint64 &containers);
    bool is_containers_Set() const;
    bool is_containers_Valid() const;

    qint64 getCreated() const;
    void setCreated(const qint64 &created);
    bool is_created_Set() const;
    bool is_created_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QMap<QString, QString> getLabels() const;
    void setLabels(const QMap<QString, QString> &labels);
    bool is_labels_Set() const;
    bool is_labels_Valid() const;

    QString getParentId() const;
    void setParentId(const QString &parent_id);
    bool is_parent_id_Set() const;
    bool is_parent_id_Valid() const;

    QList<QString> getRepoDigests() const;
    void setRepoDigests(const QList<QString> &repo_digests);
    bool is_repo_digests_Set() const;
    bool is_repo_digests_Valid() const;

    QList<QString> getRepoTags() const;
    void setRepoTags(const QList<QString> &repo_tags);
    bool is_repo_tags_Set() const;
    bool is_repo_tags_Valid() const;

    qint64 getSharedSize() const;
    void setSharedSize(const qint64 &shared_size);
    bool is_shared_size_Set() const;
    bool is_shared_size_Valid() const;

    qint64 getSize() const;
    void setSize(const qint64 &size);
    bool is_size_Set() const;
    bool is_size_Valid() const;

    qint64 getVirtualSize() const;
    void setVirtualSize(const qint64 &virtual_size);
    bool is_virtual_size_Set() const;
    bool is_virtual_size_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_containers;
    bool m_containers_isSet;
    bool m_containers_isValid;

    qint64 m_created;
    bool m_created_isSet;
    bool m_created_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QMap<QString, QString> m_labels;
    bool m_labels_isSet;
    bool m_labels_isValid;

    QString m_parent_id;
    bool m_parent_id_isSet;
    bool m_parent_id_isValid;

    QList<QString> m_repo_digests;
    bool m_repo_digests_isSet;
    bool m_repo_digests_isValid;

    QList<QString> m_repo_tags;
    bool m_repo_tags_isSet;
    bool m_repo_tags_isValid;

    qint64 m_shared_size;
    bool m_shared_size_isSet;
    bool m_shared_size_isValid;

    qint64 m_size;
    bool m_size_isSet;
    bool m_size_isValid;

    qint64 m_virtual_size;
    bool m_virtual_size_isSet;
    bool m_virtual_size_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImageSummary)

#endif // OAIImageSummary_H
