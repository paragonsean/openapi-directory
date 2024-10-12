/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIJsonPatchOperation.h
 *
 * The Json Patch definition.
 */

#ifndef OAIJsonPatchOperation_H
#define OAIJsonPatchOperation_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIJsonPatchOperation : public OAIObject {
public:
    OAIJsonPatchOperation();
    OAIJsonPatchOperation(QString json);
    ~OAIJsonPatchOperation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getFrom() const;
    void setFrom(const QString &from);
    bool is_from_Set() const;
    bool is_from_Valid() const;

    QString getOp() const;
    void setOp(const QString &op);
    bool is_op_Set() const;
    bool is_op_Valid() const;

    QString getPath() const;
    void setPath(const QString &path);
    bool is_path_Set() const;
    bool is_path_Valid() const;

    OAIObject getValue() const;
    void setValue(const OAIObject &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_from;
    bool m_from_isSet;
    bool m_from_isValid;

    QString m_op;
    bool m_op_isSet;
    bool m_op_isValid;

    QString m_path;
    bool m_path_isSet;
    bool m_path_isValid;

    OAIObject m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIJsonPatchOperation)

#endif // OAIJsonPatchOperation_H
