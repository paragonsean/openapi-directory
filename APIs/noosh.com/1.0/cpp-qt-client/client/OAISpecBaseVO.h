/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISpecBaseVO.h
 *
 * Java type: com.noosh.nooshapi.vo.SpecBaseVO
 */

#ifndef OAISpecBaseVO_H
#define OAISpecBaseVO_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISpecBaseVO : public OAIObject {
public:
    OAISpecBaseVO();
    OAISpecBaseVO(QString json);
    ~OAISpecBaseVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getJobId() const;
    void setJobId(const qint64 &job_id);
    bool is_job_id_Set() const;
    bool is_job_id_Valid() const;

    QString getReferenceNumber() const;
    void setReferenceNumber(const QString &reference_number);
    bool is_reference_number_Set() const;
    bool is_reference_number_Valid() const;

    qint64 getSpecId() const;
    void setSpecId(const qint64 &spec_id);
    bool is_spec_id_Set() const;
    bool is_spec_id_Valid() const;

    QString getSpecName() const;
    void setSpecName(const QString &spec_name);
    bool is_spec_name_Set() const;
    bool is_spec_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_job_id;
    bool m_job_id_isSet;
    bool m_job_id_isValid;

    QString m_reference_number;
    bool m_reference_number_isSet;
    bool m_reference_number_isValid;

    qint64 m_spec_id;
    bool m_spec_id_isSet;
    bool m_spec_id_isValid;

    QString m_spec_name;
    bool m_spec_name_isSet;
    bool m_spec_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISpecBaseVO)

#endif // OAISpecBaseVO_H
