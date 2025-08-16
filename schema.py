#!/usr/bin/env python3
import graphene

class Query(graphene.ObjectType):
        # Define a field called "hello" of type String
            hello = graphene.String(description="A simple GraphQL query that returns a greeting.")

                # Resolver method for the "hello" field
                    def resolve_hello(self, info):
                                return "Hello, GraphQL!"

                            # Create the schema with Query as the root
                            schema = graphene.Schema(query=Query)


        

