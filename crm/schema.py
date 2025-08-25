import graphene
from .models import Product

class ProductType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    stock = graphene.Int()

class UpdateLowStockProducts(graphene.Mutation):
    class Output:
        updated_products = graphene.List(ProductType)
        message = graphene.String()

    def mutate(self, info):
        low_stock_products = Product.objects.filter(stock__lt=10)
        updated = []

        for product in low_stock_products:
            product.stock += 10  # simulate restocking
            product.save()
            updated.append(product)

        return UpdateLowStockProducts.Output(
            updated_products=updated,
            message=f"{len(updated)} products updated successfully."
        )

class Mutation(graphene.ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()

